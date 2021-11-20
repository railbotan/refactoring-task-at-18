import numpy as np
from PIL import Image


def get_image_array(path: str) -> np.ndarray:
    img = Image.open(path)
    return np.array(img)


def save_image(img: np.ndarray, name: str) -> None:
    res = Image.fromarray(img)
    res.save(name)


def get_brightness(x: int, y: int, img: np.ndarray, block_height: int, block_width: int, gray_step: int):
    res = np.average(img[y: y + block_height, x: x + block_width])
    return res - res % gray_step


def create_gray_mosaic(img: np.ndarray, block_height: int, block_width: int, gray_step: int) -> np.ndarray:
    print("In progress... Please, wait.")
    res_img = img.copy()

    for y in range(0, len(img), block_height):
        for x in range(0, len(img[0]), block_width):
            brightness = get_brightness(x, y, img, block_height, block_width, gray_step)
            res_img[y: y + block_height, x: x + block_width] = brightness

    return res_img


def get_step(gray_scale: int) -> int:
    if gray_scale < 1 or gray_scale > 255:
        raise ValueError(f"Number of gradations must be in [1, 255]. You input: {gray_scale}")
    gray_scale -= 1
    return int(255 / gray_scale - 1 if 255 % gray_scale == 0 else 255 / gray_scale)


original_img = get_image_array(input("Enter original image file name: "))
mosaic = create_gray_mosaic(original_img,
                            int(input("Enter mosaic block height (Example: 10): ")),
                            int(input("Enter mosaic block weight (Example: 10): ")),
                            get_step(int(input("Enter number of gradations (Example: 10, min: 1, max: 255): "))))
save_image(mosaic, input("Enter result mosaic file name: "))
