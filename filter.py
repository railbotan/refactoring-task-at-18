import numpy as np
from PIL import Image


def get_img(path):
    img = Image.open(path)
    return np.array(img)


def save_img(img, name):
    res = Image.fromarray(img)
    res.save(name)


def get_pixel_art(img, size, grayscale):
    width = len(img)
    height = len(img[1])

    for x in range(0, width, size):
        for y in range(0, height, size):
            brightness = get_brightness(img, size, x, y)
            img[x: x + size, y: y + size] = brightness - brightness % grayscale
    return img


def get_brightness(img, size, x, y):
    return np.average(img[x: x + size, y: y + size])


img = get_img("img2.jpg")
save_img(get_pixel_art(img, 10, 50), 'res.jpg')