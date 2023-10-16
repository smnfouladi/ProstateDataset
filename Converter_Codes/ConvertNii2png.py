import SimpleITK as sitk
import numpy as np
import pathlib
import os
import glob
from PIL import Image
import cv2
import imageio
import nibabel as nib



def Convertnii2png(mri_filename,foldername,mrifilename, typeimg):
    
    
    if (typeimg=='img'):
       
        Slicepath='./ExtractedSlides/imgtest/'
        train_x_path = mri_filename
        all_images=glob.glob(train_x_path)
        for i in range(len(all_images)):
            image_array = nib.load(all_images[i]).get_data()    
            total_slices=image_array.shape[2]    
        
            for j in range(0,total_slices):
                data= np.rot90(image_array[:,:,j])    
                
                #image_name ="Image"+format(str(i))+"Slice"+format(str(j))+ ".png"
                image_name=foldername+"_"+mrifilename+'_img_'+str(j)+".png"
                print(image_name)
                imageio.imwrite(Slicepath+image_name, data)
                
    if (typeimg=='mask'):

        Slicepath='./ExtractedSlides/masktest/'
        train_x_path = mri_filename
        all_images=glob.glob(train_x_path)
        for i in range(len(all_images)):
            image_array = nib.load(all_images[i]).get_data()    
            total_slices=image_array.shape[2]    
        
            for j in range(0,total_slices):
                data= np.rot90(image_array[:,:,j])    
                
                #image_name ="Image"+format(str(i))+"Slice"+format(str(j))+ ".png"
                image_name=foldername+"_"+mrifilename+"_"+str(j)+".png"
                imageio.imwrite(Slicepath+image_name, data)
                
def loadingmask():
   
    
    desktop = pathlib.Path("./AllDb_Zone/RUNMC")
    mask_files=list(desktop.glob("*_segmentation.nii.gz"))
    img_files=list(desktop.glob("*.nii.gz"))
  
    for files in img_files:   
        firstpath=str(files)
        pathofmri=firstpath.replace('\\','/')   
        finalpath="./"+pathofmri

        
        if('_segmentation' not in finalpath):            

            for mri_filename in glob.glob(finalpath):
                
                mrinamefull=mri_filename.split("/",-1)[-1]            
                foldername=mri_filename.split("/",-2)[-2]            
                mrifilename=mrinamefull.split(".nii",1)[0]            

                Convertnii2png(mri_filename,foldername,mrifilename,'img')
                
    for files in mask_files:
        
        firstpath=str(files)
        pathofmri=firstpath.replace('\\','/')   
        finalpath="./"+pathofmri

        
        if('_segmentation' in finalpath):            

            for mri_filename in glob.glob(finalpath):
                
                mrinamefull=mri_filename.split("/",-1)[-1]            
                foldername=mri_filename.split("/",-2)[-2]            
                mrifilename=mrinamefull.split(".nii",1)[0]            

                Convertnii2png(mri_filename,foldername,mrifilename,'mask')

loadingmask()
                
