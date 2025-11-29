from PIL import Image
from numpy import array

def ft_load(path: str) -> array:
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