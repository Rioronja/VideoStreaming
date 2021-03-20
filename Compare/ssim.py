import cv2 
import time
import numpy as np
import tensorflow as tf
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def ssim(img1, img2):
    ssim1 = tf.image.ssim(img1, img2, max_val=255, filter_size=11,
                    filter_sigma=1.5, k1=0.01, k2=0.03)
    print(f'\rssim: {ssim1}', end='')
    return ssim1

img1 = cv2.imread('frame0036.jpg')
img2 = cv2.imread('frame0167.jpg')
print(ssim(img1, img2))