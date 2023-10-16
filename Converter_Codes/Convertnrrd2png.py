
import os
import nrrd # python -m pip install pynrrd
import argparse
from PIL import Image # python -m pip install Pillow
import SimpleITK as sitk
import numpy as np
import pathlib
import os
import glob
from PIL import Image
import cv2
import imageio
import nibabel as nib



#filename='./AllDb_Zone/test/Prostate3T-01-0001.nrrd'
outdir='./AllDb_Zone/test2'
fmt='png'

'''

def read_slices (filename, ext,scale=1): 
  

  if ext != 'nrrd':
    raise ValueError('Input filename must be a NRRD file')
  finalfname='./AllDb_Zone/ProstateX/Seg/'+str(filename)+'.nrrd'
  data, header = nrrd.read(finalfname)
  slices = (data * scale).astype('uint8')
  slices = slices.transpose(2, 1, 0)

  return slices
'''
def read_slices (foldername,filename, ext,scale=1): 
  

  if ext != 'nrrd':
    raise ValueError('Input filename must be a NRRD file')
  finalfname='./AllDb_Zone/ProstateX/Seg/'+foldername+"/"+str(filename)+'.nrrd'
  data, header = nrrd.read(finalfname)
  slices = (data * scale).astype('uint8')
  slices = slices.transpose(2, 1, 0)

  return slices

def main():

    desktop = pathlib.Path('./AllDb_Zone/ProstateX/Seg/')
    filename=list(desktop.glob('*/Segmentation.nrrd'))
        

    for files in filename:   
        firstpath=str(files)        
        pathofmri=firstpath.replace('\\','/')   
        finalpath='./'+pathofmri     
        
        for files in glob.glob(finalpath):          
            

            name, ext = files.split('.')[-2:]
            name = os.path.basename(name)
            foldername=files.split("/",-2)[-2]
            finalname=foldername+name
            #print(foldername)

            slices = read_slices(foldername,name,ext, 100.)

            for i, im in enumerate(slices):
                im = Image.fromarray(im).convert('RGB')
                im.save(os.path.join(outdir,finalname + '_{0:03d}'.format(i+1) + '.{0}'.format(fmt)),
                        '{0}'.format(fmt))


'''
def main():

    desktop = pathlib.Path('./AllDb_Zone/ProstateX/Seg/')
    filename=list(desktop.glob('*/*.nrrd'))
    

    for files in filename:   
        firstpath=str(files)        
        pathofmri=firstpath.replace('\\','/')   
        finalpath='./'+pathofmri      
        

        for files in glob.glob(finalpath):           
            

            name, ext = files.split('.')[-2:]
            name = os.path.basename(name)            

            slices = read_slices(name,ext, 100.)

            for i, im in enumerate(slices):
                im = Image.fromarray(im).convert('RGB')
                im.save(os.path.join(outdir, name + '_{0:03d}'.format(i+1) + '.{0}'.format(fmt)),
                        '{0}'.format(fmt))
'''
main()









    
