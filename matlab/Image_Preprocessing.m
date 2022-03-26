function [US,Center,Y_Ang_Init]=A_Image_Processing()
% A_Image_Processing
% Last Modified by A.Chan - Utter Matlab Noob, July 2019
%
% Purpose: Auto_Process takes images from US-Image Stack and CSV motion 
% capture file and converts it to an image stack that is placed within the 
% capture volume and aligned appropriately.
%
% Inputs to be updated:
% 1: Filters: More details are in the Filters.m file
%
% Inputs: User-selected CSV or MAT file
% Outputs:  Volume: Image stack aligned to capture volume
%           Workspace: Location of capture volume
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
display('A.1 Data Import')
[filename, pathname]=uigetfile('*.mat','Select .mat file');
[US_Raw, Mocap]=Import_Data(filename,pathname);
%% Phase 1: Surface Augmentation and Verticut
display('A.2 Surface Augmentation and Verticut')
Filt_Tog=struct('M',0,'C',1,...
                'H',0,'Q',0,...
                'V',1,'G',1);
Filt_Val=struct('M',[1,1],...           %Median Blur
                'C',[0.6,0.8,0,1],...   %Contrast Filter
                'H',[1],...             %Tophat Filter
                'Q',[5,0.6],...         %Quantization
                'G',[3]);               %Averaging

parfor k=1:size(Mocap,1)
    US_Raw(:,:,k)=Filters(US_Raw(:,:,k),Filt_Tog,Filt_Val);
end

[US, Center]=Realignment(US_Raw, Mocap);

Y_Ang_Init=round(mean(Mocap(:,7)),0);
%C=Center
US=permute(US,[1 3 2]); %Rotate to process in other direction (tried 2,3,1)

%% Phase 2: Surface Smoothing
[~, ~, N_Frames_A]=size(US);

display('A.3 Surface Smoothing')
Filt_Tog=struct('M',0,'C',0,...
                'H',0,'Q',1,...
                'V',0,'G',1);
Filt_Val=struct('M',[2,2],...           %Median Blur
                'C',[0.6,0.8,0,1],...   %Contrast Filter
                'H',[1],...             %Tophat Filter
                'Q',[5,0.8],...         %Quantization
                'G',[2]);               %Averaging
parfor k=1:N_Frames_A
    US(:,:,k)=Filters(US(:,:,k),Filt_Tog,Filt_Val);
end

display('A.4 Pixel Filter')
US=permute(US,[1 3 2]);
US=Vol_Pixel_Filter(US,20);
save('test.mat', "US")
%US(:,230:end,:)=0; %Temp Cropper
display('(A) Image Processing Complete')

%Vol_Write(US,'AAUSD')
%Transform=Calibrate(US, Center);
%Transform=2*Transform; %2X scaling.
%Heat_US=Vol2Heat(US);
%figure(3)
%imagesc(Heat_US);
