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
            brightness = get_brightness(height, img, size, width, x, y)
            for i in range(x, min(x + size, width)):
                for j in range(y, min(y + size, height)):
                    img[i][j][0] = img[i][j][1] = img[i][j][2] = brightness - brightness % grayscale

    return img


def get_brightness(height, img, size, width, x, y):
    brightness = 0
    for i in range(x, min(x + size, width)):
        for j in range(y, min(y + size, height)):
            brightness += sum(int(color) for color in img[i][j]) // 3
    brightness = brightness // (size * size)
    return brightness


img = get_img("img2.jpg")
save_img(get_pixel_art(img, 10, 50), 'res.jpg')