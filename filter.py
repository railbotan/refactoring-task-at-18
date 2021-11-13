import numpy as np
from PIL import Image


def get_image_array(path: str) -> np.ndarray:
    img = Image.open(path)
    return np.array(img)


def save_image(img: np.ndarray, name: str) -> None:
    res = Image.fromarray(img)
    res.save(name)


def get_brightness(x: int, y: int, img: np.ndarray, pixel_height: int, pixel_width: int, gray_step: int):
    res = 0
    for height in range(y, y + pixel_height):
        for width in range(x, x + pixel_width):
            channel_1 = int(img[height][width][0])
            channel_2 = int(img[height][width][1])
            channel_3 = int(img[height][width][2])
            res += (channel_1 + channel_2 + channel_3) / 3
    res = res // (pixel_height * pixel_width)
    return res - res % gray_step


def create_gray_mosaic(img: np.ndarray, pixel_height: int, pixel_width: int, gray_step: int) -> np.ndarray:
    res_img = img.copy()
    img_height = len(img)
    img_width = len(img[1])

    for y in range(0, img_height, pixel_height):
        for x in range(0, img_width, pixel_width):
            brightness = get_brightness(x, y, img, pixel_height, pixel_width, gray_step)
            for height in range(y, y + pixel_height):
                for width in range(x, x + pixel_width):
                    res_img[height][width][0] = brightness
                    res_img[height][width][1] = brightness
                    res_img[height][width][2] = brightness

    return res_img


original_img = get_image_array("img2.jpg")
mosaic = create_gray_mosaic(original_img, 10, 10, 50)
save_image(mosaic, 'res.jpg')
