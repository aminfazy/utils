
# coding: utf-8

# In[1]:



from optparse import OptionParser as op
import cv2
import numpy as np
import re
import os
import sys
import subprocess
import pdb



# In[2]:


input_video_file = 'vid.mp4'
output_video_file = 'output.mp4'
img_path = 'input/' 
output_path = 'output/'

print img_path
print output_path


# In[3]:


os.system("bash -c ls -l")


# In[4]:



frame_rate=24


# In[5]:


def convert_to_images():
    cam = cv2.VideoCapture(input_video_file)
    counter = 0
    while True:
        flag, frame = cam.read()
        if flag:
            cv2.imwrite(os.path.join(img_path, str(counter)+'.jpg'),frame)
            counter = counter + 1
        else:
            break
        if cv2.waitKey(1) == 27:
            break
            # press esc to quit
    cv2.destroyAllWindows()


# In[6]:


convert_to_images()


# In[7]:


def get_file_names(search_path):
        for (dirpath, _, filenames) in os.walk(search_path):
                for filename in filenames:
                        yield filename #os.path.join(dirpath, filename)



# In[8]:



list_files = sorted(get_file_names(img_path), key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

img0 = cv2.imread(os.path.join(img_path,'0.jpg'))
height , width , layers =  img0.shape
print len(list_files)
print img0.shape
print list_files


# In[9]:


# fourcc = cv2.cv.CV_FOURCC(*'mp4v')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#fourcc = cv2.cv.CV_FOURCC(*'XVID')


# In[10]:


videowriter = cv2.VideoWriter(output_video_file,fourcc, frame_rate, (width,height))


# In[11]:


for f in list_files:
    print("saving..." + f)
    impath=os.path.join('/home/fazy/Desktop/new_work/keras-frcnn-obj-count/input', f)
    print impath
    img = cv2.imread(impath)
    #img=np.rollaxis(img,2,0)
    print img.shape
    videowriter.write(img)
    print("saving done ..." + f)

videowriter.release()
cv2.destroyAllWindows()

