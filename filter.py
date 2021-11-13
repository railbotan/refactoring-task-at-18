import numpy as np
from PIL import Image


def get_image_array(path: str) -> np.ndarray:
    img = Image.open(path)
    return np.array(img)


def save_image(img: np.ndarray, name: str) -> None:
    res = Image.fromarray(img)
    res.save(name)


def get_brightness(x: int, y: int, img: np.ndarray, pixel_height: int, pixel_width: int, gray_step: int):
    res = np.average(img[y: y + pixel_height, x: x + pixel_width])
    return res - res % gray_step


def create_gray_mosaic(img: np.ndarray, pixel_height: int, pixel_width: int, gray_step: int) -> np.ndarray:
    res_img = img.copy()

    for y in range(0, len(img), pixel_height):
        for x in range(0, len(img[0]), pixel_width):
            brightness = get_brightness(x, y, img, pixel_height, pixel_width, gray_step)
            res_img[y: y + pixel_height, x: x + pixel_width] = brightness

    return res_img


original_img = get_image_array("img2.jpg")
mosaic = create_gray_mosaic(original_img, 10, 10, 50)
save_image(mosaic, 'res.jpg')
