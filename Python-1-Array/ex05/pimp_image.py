import numpy as np
from numpy import array
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """
    Invert the colors of the image (255 - pixel)
    """
    try:
        new_img = np.zeros(array.shape, dtype=array.dtype)
        new_img = 255 - array
        plt.imshow(new_img)
        plt.show()
    except Exception as e:
        print(e)


def ft_red(array) -> array:
    """
    Only keep the red channel: the others are set to zero.
    """
    try:
        new_img = np.zeros(array.shape, dtype=array.dtype)
        new_img[:, :, 0] = array[:, :, 0]
        new_img[:, :, 1] = 0
        new_img[:, :, 2] = 0
        plt.imshow(new_img)
        plt.show()
    except Exception as e:
        print(e)


def ft_green(array) -> array:
    """
    Only keep the green channel: the others are set to zero.
    """
    try:
        new_img = np.zeros(array.shape, dtype=array.dtype)
        new_img[:, :, 0] = 0
        new_img[:, :, 1] = array[:, :, 1]
        new_img[:, :, 2] = 0
        plt.imshow(new_img)
        plt.show()
    except Exception as e:
        print(e)


def ft_blue(array) -> array:
    """
    Only keep the blue channel: the others are set to zero.
    """
    try:
        new_img = np.zeros(array.shape, dtype=array.dtype)
        new_img[:, :, 0] = 0
        new_img[:, :, 1] = 0
        new_img[:, :, 2] = array[:, :, 2]
        plt.imshow(new_img)
        plt.show()
    except Exception as e:
        print(e)


def ft_grey(array) -> array:
    """
    Converts the image to grayscale using the green channel.
    """
    try:
        new_img = np.zeros(array.shape, dtype=array.dtype)
        new_img[:, :, 0] = array[:, :, 1]
        new_img[:, :, 1] = array[:, :, 1]
        new_img[:, :, 2] = array[:, :, 1]
        plt.imshow(new_img)
        plt.show()
    except Exception as e:
        print(e)
