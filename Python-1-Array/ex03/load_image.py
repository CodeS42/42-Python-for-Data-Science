from PIL import Image
from numpy import array

def ft_load(path: str) -> array:
    """
    Load an image from the given file path.
    Convert it to RGB.
    Prints
        - The shape of the loaded image (height, width, channels).
        - The 3D array

    Parameters
        path: Path to the image file to load.

    Returns
        The loaded image as a 3D array.

    Raises
        TypeError: If the provided path is not a string.
        ValueError: If the image format is not JPG or JPEG.
    """
    if not isinstance(path, str):
        raise TypeError("Path must be a string.")
    img = Image.open(path)
    format_img = img.format.upper()
    if not (format_img == "JPG" or format_img == "JPEG"):
        raise ValueError("Unsupported format.")
    img = img.convert("RGB")
    img_array = array(img)
    print(f"The shape of image is : {img_array.shape}")
    print(img_array)

    return img_array
