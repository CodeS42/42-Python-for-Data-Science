from PIL import Image
from numpy import array


def ft_load(path: str) -> array:
    """
    Load an image from a file and convert it to an RGB array.

    This function first checks that the provided path is a string and that the
    image format is supported (JPG or JPEG). It then opens the file, converts
    the image to RGB mode, and returns it as a 3D array.

    If the path is invalid or the format is not allowed, an exception is
    raised.
    """
    if not isinstance(path, str):
        raise TypeError("TypeError: Path must be a string.")
    img = Image.open(path)
    format_img = img.format.upper()
    if not (format_img == "JPG" or format_img == "JPEG"):
        raise ValueError("ValueError: Unsupported format.")
    img = img.convert("RGB")
    img_array = array(img)

    return img_array
