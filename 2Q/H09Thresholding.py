#Veve Machajdiková podzravuje

import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io
import skimage.filters



image_stack = skimage.io.imread('https://github.com/guiwitz/PyImageCourse_beginner/raw/master/images/46658_784_B12_1.tif')
image_nuclei = image_stack[:,:,2]
image_cells =  image_stack[:,:,1]
image_stringything =  image_stack[:,:,0]

my_otsu_threshold2 = skimage.filters.threshold_otsu(image_nuclei)
my_otsu_threshold1 = skimage.filters.threshold_otsu(image_cells)
my_otsu_threshold0 = skimage.filters.threshold_otsu(image_stringything)



mask2 = image_nuclei > my_otsu_threshold2
mask1 = image_cells > my_otsu_threshold1
mask0 = image_stringything > my_otsu_threshold0

mask = mask0 + mask1 #mask combinations


plt.imshow(mask, cmap = 'gray')
plt.show()
plt.imshow(image_nuclei, cmap='gray')
plt.show()


