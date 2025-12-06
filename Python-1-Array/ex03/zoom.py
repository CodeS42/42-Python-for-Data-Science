from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(img, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """
    Extract a zoomed region from an image array and display it.

    This function slices the image using the provided coordinate ranges
    for height, width, and channels, producing a smaller sub-image.
    It prints the shape of the resulting array and shows the zoomed region
    using matplotlib in grayscale.

    The extracted zoomed image is displayed directly.
    """
    zoomed_img = img[start_y:end_y, start_x:end_x, channel_start:channel_end]
    zoomed_img_shape = zoomed_img.shape
    print(f"New shape after slicing: {zoomed_img_shape} or \
{zoomed_img_shape[:2]}")
    print(zoomed_img)
    plt.imshow(zoomed_img[:, :, 0], cmap="gray")
    plt.show()


def main():
    """
    Main function to load an image, display its information, and perform
    a zoom.

    - Loads 'animal.jpeg' using ft_load()
    - Prints the original image's shape and pixel values
    - Calls ft_zoom() with fixed slicing coordinates
    - Handles any exception and prints an error message
    """
    try:
        img = ft_load("animal.jpeg")
        print(f"The shape of image is : {img.shape}")
        print(img)
        ft_zoom(img, 100, 500, 450, 850, 0, 1)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
