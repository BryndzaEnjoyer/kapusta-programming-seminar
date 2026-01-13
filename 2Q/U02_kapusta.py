# --------------------------------------------------
# Image processing – cleaned version
# --------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import random as rd
import skimage.io
import skimage.filters


# --------------------------------------------------
# BASIC IMAGE LOADING & CROPPING
# --------------------------------------------------

# Load image stack
image_stack = skimage.io.imread(
    'https://github.com/guiwitz/PyImageCourse_beginner/raw/master/images/46658_784_B12_1.tif'
)

# Crop region
y1, y2 = 1250, 1750
x1, x2 = 300, 800
image_nuclei = image_stack[y1:y2, x1:x2, 2]

X = x2 - x1
Y = y2 - y1


# --------------------------------------------------
# KERNEL INITIALIZATION
# --------------------------------------------------

size = 20
kerk = np.zeros((size, size))
finalkerk = np.zeros((size, size))

kerk[10, 10] = 255


# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def random_dots(n, image):
    """Add random white pixels (noise) to image."""
    noisy = image.copy()
    for _ in range(n):
        noisy[rd.randint(0, size - 1), rd.randint(0, size - 1)] = 255
    return noisy


def mean_smoothing(image):
    """Apply mean (3x3 average) smoothing."""
    result = image.copy()

    for y in range(1, size - 1):
        for x in range(1, size - 1):
            neighborhood = image[y-1:y+2, x-1:x+2]
            result[y, x] = np.mean(neighborhood)

    return result


def gaussian_smoothing(image, n):
    """Apply Gaussian smoothing n times."""
    kernel = np.array([
        [1, 4, 1],
        [4, 8, 4],
        [1, 4, 1]
    ])

    result = image.copy()

    for _ in range(n):
        temp = result.copy()
        for y in range(1, image.shape[0] - 1):
            for x in range(1, image.shape[1] - 1):
                region = temp[y-1:y+2, x-1:x+2]
                result[y, x] = np.sum(region * kernel) / 28

    return result


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

plt.imshow(random_dots(50, kerk), cmap='gray')
plt.title("Random Dots")
plt.show()

plt.imshow(mean_smoothing(kerk), cmap='gray')
plt.title("Mean Smoothing")
plt.show()

plt.imshow(gaussian_smoothing(kerk, 100), cmap='gray')
plt.title("Gaussian Smoothing (Kernel)")
plt.show()

plt.imshow(gaussian_smoothing(image_nuclei, 10), cmap='gray')
plt.title("Gaussian Smoothing (Image)")
plt.show()


# --------------------------------------------------
# OTSU THRESHOLDING
# --------------------------------------------------

image_nuclei = image_stack[:, :, 2]
image_cells = image_stack[:, :, 1]
image_stringy = image_stack[:, :, 0]

t_nuclei = skimage.filters.threshold_otsu(image_nuclei)
t_cells = skimage.filters.threshold_otsu(image_cells)
t_stringy = skimage.filters.threshold_otsu(image_stringy)

mask = (image_cells > t_cells) | (image_stringy > t_stringy)

plt.imshow(mask, cmap='gray')
plt.title("Combined Mask")
plt.show()

plt.imshow(image_nuclei, cmap='gray')
plt.title("Nuclei Channel")
plt.show()
