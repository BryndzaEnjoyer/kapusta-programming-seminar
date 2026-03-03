# --------------------------------------------------
# Image processing pipeline
# Original → Crop → Threshold → Gaussian → Median
# --------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import skimage.io
import skimage.filters


# --------------------------------------------------
# LOAD IMAGE
# --------------------------------------------------

image = skimage.io.imread(
    'https://github.com/BryndzaEnjoyer/kapusta-programming-seminar/blob/main/FOTO-5-768x567.jpeg?raw=true'
)

# Convert to grayscale if RGB
if image.ndim == 3:
    image_gray = image.mean(axis=2)
else:
    image_gray = image


# --------------------------------------------------
# FUNCTIONS (WITH DOCSTRINGS)
# --------------------------------------------------

def crop_image(image, r1, r2, c1, c2):
    """
    Crop a rectangular region from an image.

    Parameters
    ----------
    image : numpy.ndarray
        Input image.
    r1, r2 : int
        Row range.
    c1, c2 : int
        Column range.

    Returns
    -------
    numpy.ndarray
        Cropped image.
    """
    return image[r1:r2, c1:c2]


def threshold_segmentation(image, threshold):
    """
    Apply threshold segmentation.

    Parameters
    ----------
    image : numpy.ndarray
        Grayscale image.
    threshold : int or float
        Threshold value.

    Returns
    -------
    numpy.ndarray
        Binary image.
    """
    return image > threshold


def gaussian_filter(image, iterations):
    """
    Apply Gaussian smoothing using a 3x3 kernel.

    Parameters
    ----------
    image : numpy.ndarray
        Input image.
    iterations : int
        Number of smoothing iterations.

    Returns
    -------
    numpy.ndarray
        Smoothed image.
    """
    kernel = np.array([
        [1, 4, 1],
        [4, 8, 4],
        [1, 4, 1]
    ])

    result = image.copy()

    for _ in range(iterations):
        temp = result.copy()
        for y in range(1, image.shape[0] - 1):
            for x in range(1, image.shape[1] - 1):
                region = temp[y-1:y+2, x-1:x+2]
                result[y, x] = np.sum(region * kernel) / 28

    return result


def median_filter(image):
    """
    Apply median filter using a 3x3 neighborhood.

    Parameters
    ----------
    image : numpy.ndarray
        Input image.

    Returns
    -------
    numpy.ndarray
        Median-filtered image.
    """
    result = image.copy()

    for y in range(1, image.shape[0] - 1):
        for x in range(1, image.shape[1] - 1):
            region = image[y-1:y+2, x-1:x+2]
            result[y, x] = np.median(region)

    return result


# --------------------------------------------------
# IMAGE PROCESSING PIPELINE
# --------------------------------------------------

# 1. Crop
cropped = crop_image(image_gray, 100, 500, 100, 500)

# 2. Threshold segmentation
t = skimage.filters.threshold_otsu(cropped)
thresholded = threshold_segmentation(cropped, t)

# 3. Gaussian filter
gaussian = gaussian_filter(cropped, 20)

# 4. Median filter
median = median_filter(cropped)


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

plt.figure(figsize=(10, 8))

plt.subplot(2, 3, 1)
plt.imshow(image_gray, cmap='gray')
plt.title("Original")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(cropped, cmap='gray')
plt.title("Cropped")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(thresholded, cmap='gray')
plt.title("Threshold")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(gaussian, cmap='gray')
plt.title("Gaussian Filter")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(median, cmap='gray')
plt.title("Median Filter")
plt.axis("off")

plt.tight_layout()
plt.show()