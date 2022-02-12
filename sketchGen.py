import numpy as np
import imageio
import scipy.ndimage
import cv2

img="photo.jpg"
s=imageio.imread(img)

def grayScale(rgb):
    return np.dot(rgb[...,:3], [0.2, 0.2, 0.2])

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype(np.uint8)

s = imageio.imread(img)
g=grayScale(s)
i=255-g
b=scipy.ndimage.filters.gaussian_filter(i, sigma=15)
r=dodge(b,g)
cv2.imwrite("sketch21.jpg",r)
print("Photo has been sketched :D")
print(np.filters)
print(scipy.ndimage.filters)