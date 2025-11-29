from load_image import ft_load
from numpy import array

def slice_me_3D(img: array, start_y: int, end_y: int, start_x: int, end_x: int, channel_y: int, channel_x: int):
    try:
        if not all(isinstance(elem, int) for elem in (start_y, end_y, start_x, end_x, channel_y, channel_x)):
            raise TypeError("")
        new_img = img[start_y:end_y, start_x:end_x, 0:1]
        new_img_shape = new_img.shape
        # if len(new_img_shape)
        print(f"New shape after slicing: {new_img_shape}")
        return new_img
    except Exception as e:
        print(f"Error: {e}")
        return None

def ft_zoom(path: str) -> array:
    img_array = ft_load(path)
    # if img_array == None:
    #     return None
    print(img_array)
    print(slice_me_3D(img_array, 0, 400, 0, 400, 0, 1))
    

def main():
    ft_zoom("animal.jpeg")

if __name__ == "__main__":
    main()