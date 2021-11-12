import os
import numpy as np
from PIL import Image, UnidentifiedImageError


def load_img_as_array(path: str) -> np.ndarray:
    if os.path.isfile(path):
        try:
            img = Image.open(path)
            return np.array(img)
        except UnidentifiedImageError:
            raise TypeError("Incorrect file type.")
    raise FileExistsError("This file doesn't exist.")


def convert_to_gray_pixel_art(img: np.ndarray, pixel_size: int = 10, grayscale: int = 50) -> np.ndarray:
    for x in range(0, len(img), pixel_size):
        for y in range(0, len(img[0]), pixel_size):
            brightness = np.average(img[x: x + pixel_size, y: y + pixel_size])
            img[x: x + pixel_size, y: y + pixel_size] = brightness - brightness % grayscale

    return img


def save_img(img: np.ndarray, filename: str) -> None:
    Image.fromarray(img).save(filename)


def main() -> None:
    img = load_img_as_array("img2.jpg")
    gray_image = convert_to_gray_pixel_art(img, 10, 50)
    save_img(gray_image, "res.jpg")


if __name__ == "__main__":
    main()
