import os

import pydicom as dicom
import shutil
import png
import pathlib
import glob


dcm_folders='./AllDb_Zone/ProstateX/MainData/'
png_folders='./AllDb_Zone/test/'

def dcm_to_png(dcm_file, png_file):
    
    
    ''' Function to convert from a DCM image to png
        @param dcm_file: An opened file like object to read te dicom data
        @param png_file: An opened file like object to write the png data
    '''

    # Extracting data from the dcm file
    plan = dicom.read_file(dcm_file)
    shape = plan.pixel_array.shape    

    image_2d = []
    max_val = 0
    for row in plan.pixel_array:
        pixels = []
        for col in row:
            pixels.append(col)
            if col > max_val: max_val = col
        image_2d.append(pixels)

    # Rescaling grey scale between 0-255
    image_2d_scaled = []
    for row in image_2d:
        row_scaled = []
        for col in row:
            col_scaled = int((float(col) / float(max_val)) * 255.0)
            row_scaled.append(col_scaled)
        image_2d_scaled.append(row_scaled)

    # Writing the PNG file
    w = png.Writer(shape[1], shape[0], greyscale=True)    
    w.write(png_file, image_2d_scaled)

def GeneratePath(foldername,mrifilename):

    dcm_file_path=dcm_folders+foldername+"/"+mrifilename+".dcm"
    png_file_path=png_folders+foldername+mrifilename+".png"

    dcm_file = open(dcm_file_path, 'rb')
    png_file = open(png_file_path, 'wb')

    dcm_to_png(dcm_file, png_file)

    png_file.close()
    
    
def LoadIMG():
   
    
    desktop = pathlib.Path("./AllDb_Zone/ProstateX/MainData/")
    
    img_files=list(desktop.glob("*/*.dcm"))
  
    for files in img_files:   
        firstpath=str(files)
        pathofmri=firstpath.replace('\\','/')   
        finalpath="./"+pathofmri     
                
        for mri_filename in glob.glob(finalpath):
            
            mrinamefull=mri_filename.split("/",-1)[-1]            
            foldername=mri_filename.split("/",-2)[-2]            
            mrifilename=mrinamefull.split(".dcm",1)[0]
            GeneratePath(foldername,mrifilename)

            
LoadIMG()
