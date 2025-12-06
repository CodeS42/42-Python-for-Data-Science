from PIL import Image
from numpy import array


def ft_load(path: str) -> array:
    """
    Load an image from a file and convert it to an RGB array.

    This function first checks that the provided path is a string and that the
    image format is supported (JPG or JPEG). It then opens the file, converts
    the image to RGB mode, and returns it as a 3-dimensional array.

    If the path is invalid or the format is not allowed, an exception is
    raised.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")
        img = Image.open(path)
        format_img = img.format.upper()
        if not (format_img == "JPG" or format_img == "JPEG"):
            raise ValueError("Unsupported format.")
        img = img.convert("RGB")
        img_array = array(img)
        print(f"The shape of image is : {img_array.shape}")
        return img_array
    except Exception as e:
        print("Error: ", e)
        return None
