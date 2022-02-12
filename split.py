 import glob

 depths = glob.glob('./depths/*.png')

with open('./train.txt','r') as f:
    train = list(f)

for i in range(len(train)-1):
    train[i]=train[i][:-1]

for i in range(len(depths)):
    depths[i]=depths[i][9:-4]

import os
import shutil

for i in depths:
    if i in train:
        shutil.move('./depths/'+i+'.png', './depths/train/'+i+'_GT.png')
        shutil.move('./images/'+i+'.jpg', './images/test/'+i+'_RGB.jpg')
    else:
        shutil.move('./depths/'+i+'.png', './depths/test/'+i+'_GT.png')
        shutil.move('./images/'+i+'.jpg', './images/train/'+i+'_RGB.jpg')
      