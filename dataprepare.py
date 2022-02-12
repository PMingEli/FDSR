import numpy as np
import argparse
import glob
from imageio import imread

parser = argparse.ArgumentParser()
parser.add_argument('--train_rgb_files',  default='./data/images/train/*.jpg', help='folder name of train rgb image')
parser.add_argument('--test_rgb_files',  default='./data/images/test/*.jpg', help='folder name of test rgb image')
parser.add_argument('--train_depth_files',  default='./data/depths/train/*.png', help='folder name of train depth image')
parser.add_argument('--test_depth_files',  default='./data/depths/test/*.png', help='folder name of test depth image')
opt = parser.parse_args()

depths = []
images = []

# 保存训练集的深度图像以及彩色图像数据
train_depths = glob.glob(opt.train_depth_files)
train_depths = sorted(train_depths)
train_images = glob.glob(opt.train_rgb_files)
train_images = sorted(train_images)
for i in range (len(train_depths)):
   depth = imread(train_depths[i]).astype('float32')
   depth_min = np.min(depth)
   depth_max = np.max(depth)
   depth = (depth - depth_min) / (depth_max - depth_min)
   depths.append(depth)

   image = imread(train_images[i]).astype('float32') / 255.0
   # image = np.transpose(image, (2, 0, 1))
   images.append(image)

np.save("./data/npy/train_depth_split.npy", depths)
np.save("./data/npy/train_images_split.npy", images)

depths.clear()
images.clear()

# 保存验证集的深度图像以及彩色图像数据
test_depths = glob.glob(opt.test_depth_files)
test_depths = sorted(test_depths)
test_images = glob.glob(opt.test_rgb_files)
test_images = sorted(test_images)
for i in range (len(test_depths)):
   depth = imread(test_depths[i]).astype('float32')
   depth_min = np.min(depth)
   depth_max = np.max(depth)
   depth = (depth - depth_min) / (depth_max - depth_min)
   depths.append(depth)

   image = imread(test_images[i]).astype('float32') / 255.0
   # image = np.transpose(image, (2, 0, 1))
   images.append(image)

np.save("./data/npy/test_depth.npy", depths)
np.save("./data/npy/test_images.npy", images)

# 保存验证集的minmax值，用于验证时的归一化操作
test_files_minmax = glob.glob(opt.test_depth_files)
test_files_minmax = sorted(test_files_minmax)
minmax_all = []
for i in range (len(test_files_minmax)):
   minmax = []
   lr = imread(test_files_minmax[i]).astype('float32')
   minmax.append(np.min(lr))
   minmax.append(np.max(lr))
   minmax_all.append(minmax)

np.save("./data/npy/test_minmax.npy",np.array(minmax_all))



# for file in os.listdir(train_depth_path):
#    d1 = cv2.imread('./data/nyu_depths/train/{0}'.format(file),0).astype('float32')
#    min = np.min(d1)
#    max = np.max(d1)
#    d1 = (d1-min)/(max-min)
#    depth_data.append(d1)

# train_depth_data = np.array(depth_data)

# np.save("./data/npy/train_depth_split.npy", train_depth_data)

# for file in os.listdir(train_image_path):
#    image = cv2.imread('./data/nyu_images/train/{0}'.format(file)).astype('float32') / 255.0
#    # image = np.transpose(image, (2, 0, 1))
#    image_data.append(image)

# train_image_data = np.array(image_data)

# np.save("./data/npy/train_images_split.npy", train_image_data)

# depth_data.clear()
# # image_data.clear()

# for file in os.listdir(test_depth_path):
#    d1 = cv2.imread('./data/nyu_depths/test/{0}'.format(file),0).astype('float32')
#    min = np.min(d1)
#    max = np.max(d1)
#    d1 = (d1-min)/(max-min)
#    depth_data.append(d1)

# test_depth_data = np.array(depth_data)

# np.save("./data/npy/test_depth.npy", test_depth_data)

# for file in os.listdir(test_image_path):
#    image = cv2.imread('./data/nyu_images/test/{0}'.format(file)).astype('float32') / 255.0
#    # image = np.transpose(image, (2, 0, 1))
#    image_data.append(image)

# test_image_data = np.array(image_data)

# np.save("./data/npy/test_images.npy", test_image_data)

