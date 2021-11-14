import numpy as np
from PIL import Image


def img_to_nparr(path):
    img = Image.open(path)
    return np.array(img)


def save_img_from_nparr(img, name):
    res = Image.fromarray(img)
    res.save(name)


def create_pixel_art(img, size, grayscale):
    width = len(img)
    height = len(img[1])

    for x in range(0, width, size):
        for y in range(0, height, size):
            brightness = get_average_brightness(img, size, x, y)
            for x1 in range(x, min(x + size, width)):
                for y1 in range(y, min(y + size, height)):
                    img[x1][y1][0] = img[x1][y1][1] = img[x1][y1][2] = brightness - brightness % grayscale

    return img


def get_average_brightness(img, size, x, y):
    width = len(img)
    height = len(img[1])
    brightness = 0
    for i in range(x, min(x + size, width)):
        for j in range(y, min(y + size, height)):
            brightness += sum(int(color) for color in img[i][j]) // 3
    brightness = brightness // (size * size)
    return brightness


img = img_to_nparr("img2.jpg")
save_img_from_nparr(create_pixel_art(img, 10, 50), 'res.jpg')
