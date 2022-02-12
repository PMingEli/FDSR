# -*- coding: utf-8 -*-
import numpy as np
import h5py
import os
from PIL import Image
 
f=h5py.File("nyu_depth_v2_labeled.mat")
depths=f["depths"]
depths=np.array(depths)
 
path_converted='./depths/'
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)
 
max = depths.max()
print(depths.shape)
print(depths.max())
print(depths.min())
 
depths = depths / max * 255
depths = depths.transpose((0,2,1))
 
print(depths.max())
print(depths.min())
 
for i in range(len(depths)):
    print(str(i) + '.png')
    depths_img= Image.fromarray(np.uint8(depths[i]))
    depths_img = depths_img.transpose(Image.FLIP_LEFT_RIGHT)
    iconpath=path_converted + str(i)+'.png'
    depths_img.save(iconpath, 'PNG', optimize=True)