#Juro Uhlík pozdravuje

import numpy as np
import matplotlib.pyplot as plt
import random as rd
from skimage import io
import skimage.io

y1=1250
y2=1750
x1=300
x2=800

image_stack = skimage.io.imread('https://github.com/guiwitz/PyImageCourse_beginner/raw/master/images/46658_784_B12_1.tif')
image_nuclei = image_stack[x1:x2,y1:y2,2]  

X = x2 - x1
Y= y2 - y1

x=20
y=20

a=[]
for i in range(20*20):
    a.append(0)
kerk=np.array(a)  
kerk=kerk.reshape(20,20)
kerk[10,10]=255






def randomdots(n, kerk):
    """
    Adds random white pixels (noise) to an image.

    Parameters
    ----------
    n : int
        Number of random pixels to add.
    kerk : numpy.ndarray
        2D grayscale image array.

    Returns
    -------
    numpy.ndarray
        Image with added random noise.
    """
    for i in range(n):
        kerk[rd.randint(0,19),rd.randint(0,19)]= 255
    return kerk
        


def meansmoothing(kerk, finalkerk):
    """
    Applies mean (average) smoothing using a 3x3 kernel.

    Parameters
    ----------
    kerk : numpy.ndarray
        Input grayscale image.
    finalkerk : numpy.ndarray
        Output image array to store the smoothed result.

    Returns
    -------
    numpy.ndarray
        Mean-smoothed image.
    """
  
    
    for yy in range(1,19):
        for z in range(1,19):
            arr = kerk[yy-1:yy+2, z-1:z+2].copy()     
        
        #averaging
            a=0
            for y in range(3):
                for x in range(3):
                    a=a+arr[x,y]
            av=a/9
            finalkerk[yy, z] =av
    
    finalkerk[10,10]=255

    return finalkerk

def gaussianmoothing(kerk,n,X,Y):
    """
    Applies Gaussian smoothing iteratively using a 3x3 Gaussian kernel.

    Parameters
    ----------
    kerk : numpy.ndarray
        Input grayscale image.
    n : int
        Number of smoothing iterations.
    X : int
        Width of the image.
    Y : int
        Height of the image.

    Returns
    -------
    numpy.ndarray
        Gaussian-smoothed image.
    """

    finalkerk=kerk.copy()
    if n == 0:
        return finalkerk
    else:   
        for _ in range(n):

            for yy in range(1,Y-1):
                for z in range(1,X-1):
                    arr = kerk[yy-1:yy+2, z-1:z+2].copy()
                    gaus=np.array([
                        [1,4,1],
                        [4,8,4],
                        [1,4,1]
                    ])
                    arr=arr*gaus

                #averaging
                    a=0
                    for y in range(3):
                        for x in range(3):
                            a=a+arr[x,y]

                    av=a/(28)
                    finalkerk[yy, z] =av

            kerk=finalkerk.copy()
    finalkerk[0,0]=100
    
       
    return finalkerk
    



image_stack = skimage.io.imread('https://github.com/guiwitz/PyImageCourse_beginner/raw/master/images/46658_784_B12_1.tif')
image_nuclei = image_stack[y1:y2,x1:x2,2]  




n=5 #number of iterations in gaussiansmoothing
noisy = 20*np.random.rand(20,20)


plt.imshow(randomdots(50, kerk), cmap='gray')
plt.show()
plt.imshow(meansmoothing(noisy), cmap='gray')
plt.show()
plt.imshow(gaussianmoothing(noisy,n, x, y), cmap='gray')
plt.show()
plt.imshow(gaussianmoothing(image_nuclei,n,X,Y), cmap='gray')
plt.show()

