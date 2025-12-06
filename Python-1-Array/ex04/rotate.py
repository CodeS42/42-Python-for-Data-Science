from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(img, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """
    Extract a zoomed region from an image array and print information
    about it.

    This function slices the image using the provided coordinate ranges for
    height, width, and channels, producing a smaller sub-image. It prints the
    shape and the raw values of the resulting region, then returns its 2D
    representation by selecting the first channel.
    """
    new_img = img[start_y:end_y, start_x:end_x, channel_start:channel_end]
    new_img_shape = new_img.shape
    print(f"The shape of image is: {new_img_shape} or {new_img_shape[:2]}")
    print(new_img)
    return new_img[:, :, 0]


def ft_transpose(img):
    """
    Transpose a 2D image array by swapping its rows and columns.

    This function creates a new array where each pixel at position (y, x)
    in the original image is moved to position (x, y). The resulting
    transposed image has its height and width inverted. The function then
    prints the shape and the pixel values of the new array, and displays
    the transposed image in grayscale.
    """
    new_img = np.zeros((img.shape[1], img.shape[0]), dtype=img.dtype)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            new_img[x, y] = img[y, x]
    print(f"New shape after Transpose: {new_img.shape}")
    print(new_img)
    plt.imshow(new_img, cmap="gray")
    plt.show()


def main():
    """
    Main function to load the image and perform zoom.

    - Loads 'animal.jpeg' using ft_load()
    - Calls ft_zoom() with fixed slicing coordinates
    - Calls ft_transpose() to rotate the sliced image.
    - Handles any exception and prints an error message
    """
    try:
        img = ft_load("animal.jpeg")
        zoomed_img = ft_zoom(img, 100, 500, 450, 850, 0, 1)
        ft_transpose(zoomed_img)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
