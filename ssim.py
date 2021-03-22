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

def load_and_convert(filename):
    ret = cv2.imread(filename)
    ret = cv2.cvtColor(ret, cv2.COLOR_BGR2RGB)
    return ret

baseline = load_and_convert('frame0036.jpg')
ssim_v_list = []
for frame in os.listdir('.'):
    if frame.find('frame') > -1:
        img2 = load_and_convert(frame)
        fig = plt.figure()

        rows = 2 
        columns = 1

        # plt.axis('off')

        fig.add_subplot(rows, columns, 1)
        plt.imshow(baseline)
        plt.axis('off')

        fig.add_subplot(rows, columns, 2)
        ssim_v = ssim(baseline, img2)
        plt.title(f'ssim: {ssim_v:.2f}')
        plt.imshow(img2)
        plt.axis('off')

        fig.tight_layout()    
        ssim_v_list.append(ssim_v)
        plt.close()

value = np.array(ssim_v_list)
value.sort()
p = 1. * np.arange(len(value)) / (len(value) - 1)
plt.plot(value, p, color='g', linestyle=':', label="Aggregate" )
plt.savefig('ssim_cdf.jpg')
    # plt.show()
