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
        print(f"Format : {format_img}\nThe shape of image is : {img_array.shape}")
        return img_array
    except Exception as e:
        print("Error: ", e)
        return None

def main():
    # Test subject
    print(ft_load("landscape.jpg"))
    print()

    # JPEG image
    print(ft_load("animal.jpeg"))
    print()

    # Wrong type of image
    print(ft_load("animal.j"))
    print()

    # Image doesn't exist
    print(ft_load("test.jpeg"))
    print()

    # Wrong type of input
    print(ft_load(1))

if __name__ == "__main__":
    main()