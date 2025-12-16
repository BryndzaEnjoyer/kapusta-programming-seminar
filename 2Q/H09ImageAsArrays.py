import numpy as np
import matplotlib.pyplot as plt
import random as rd
from skimage import io


# Load an image from a URL and store it as a NumPy array
image = io.imread('https://cildata.crbs.ucsd.edu/media/images/13901/13901.tif')

print(image.shape)
print(type(image))


def crop_image(image, r1, r2, c1, c2):
    """
    Crop a rectangular region from an image.

    Parameters
    ----------
    image : numpy.ndarray
        Input image stored as a NumPy array.
    r1 : int
        Starting row index.
    r2 : int
        Ending row index (not included).
    c1 : int
        Starting column index.
    c2 : int
        Ending column index (not included).

    Returns
    -------
    numpy.ndarray
        Cropped portion of the image.
    """
    return image[r1:r2, c1:c2]


# Crop a 200x200 region from the image
cropped = crop_image(image, 100, 300, 100, 300)

# Increase brightness by adding 5 to all pixel values
image = image + 5

# Display the modified full image
plt.imshow(image, cmap='gray')
plt.title("Brightened Image")
plt.axis('off')
plt.show()

# Display the cropped image
plt.imshow(cropped, cmap='gray')
plt.title("Cropped Image")
plt.axis('off')
plt.show()
