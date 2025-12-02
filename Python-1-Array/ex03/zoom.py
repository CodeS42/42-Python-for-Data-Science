from load_image import ft_load
from numpy import array
import matplotlib.pyplot as plt


def slice_me_3D(img, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """
    Slice a 3D image array according to given indices.

    Parameters:
        - img: numpy array representing the image
        - start_y, end_y: row indices for slicing (height)
        - start_x, end_x: column indices for slicing (width)
        - channel_start, channel_end: start and end indices for the channels

    Returns:
        new_img: sliced image array

    Prints:
        Shape of the sliced image. If only one channel is selected, also shows
        the 2D equivalent shape.

    Raises:
        TypeError: if any index is not an integer
    """
    if not all(isinstance(elem, int) for elem in (start_y, end_y, start_x, end_x, channel_start, channel_end)):
        raise TypeError("The data for slicing must be integers.")
    new_img = img[start_y:end_y, start_x:end_x, channel_start:channel_end]
    new_img_shape = new_img.shape
    if len(new_img_shape) == 3 and new_img_shape[2] == 1:
        print(f"New shape after slicing: {new_img_shape} or {new_img_shape[:2]}")
    else:
        print(f"New shape after slicing: {new_img_shape}")
    return new_img


def ft_zoom(img_array, start_y, end_y, start_x, end_x, channel_start, channel_end):
    """
    Perform zoom on the image array and display it.

    Parameters:
        - img_array: numpy array of the loaded image
        - start_y, end_y, start_x, end_x, channel_start, channel_end: integers
        for slicing

    Prints:
        The sliced (zoomed) image array

    Displays:
        Zoomed image using matplotlib: 
            - If 1 or 2 channels are selected: grayscale
            - Otherwise: color
    """
    zoomed_img = slice_me_3D(img_array, start_y, end_y, start_x, end_x, channel_start, channel_end)
    print(zoomed_img)
    if zoomed_img.shape[2] == 1 or zoomed_img.shape[2] == 2:
        plt.imshow(zoomed_img[:, :, 0], cmap="gray")
    else:
        plt.imshow(zoomed_img)
    plt.show()
    

def main():
    """
    Main function to load the image and perform zoom.

    - Loads 'animal.jpeg' using ft_load()
    - Calls ft_zoom() with fixed slicing coordinates
    - Handles any exception and prints an error message
    """
    try:
        img = ft_load("animal.jpeg")
        ft_zoom(img, 100, 500, 450, 850, 0, 1)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
