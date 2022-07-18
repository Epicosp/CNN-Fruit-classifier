#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
from os import listdir
from os.path import isfile, join


# In[2]:


def vid_to_file(path_to_vid, save_location=):
  ''' 
  function to extract individual frames as .jpg images from an mp4 file.
  code courtesy of fireant from stack overflow
  https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
  '''

  # init video capture object, with mp4 file
  vidcap = cv2.VideoCapture(path_to_vid)

  #read the first frame of the mp4
  success,image = vidcap.read()

  # use loop to progress through each frame and save to jpg
  count = 0
  while success:
    cv2.imwrite(f'{save_location}/frame%d.jpg' % count, image)    
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1


# In[ ]:


# crop the images down to smaller size
def crop_image(path_to_image, crop_size=(300,450,900,1000)):
    """function to overwrite an image with a cropped version of the image"""
    image = Image.open(path_to_image)
    cropped_image = image.crop(crop_size)
    cropped_image.save(path_to_image)


# In[5]:


# get list of all video files
all_videos = [file for file in listdir('vid_files') if isfile(join('vid_files', file))]

for video in all_videos:
    vid_to_file(f'vid_files{video}')


# In[ ]:


all_images = [f for f in listdir('banana_images') if isfile(join('banana_images', f))]

for file in all_images:
    crop_image(f'banana_images/{file}')

