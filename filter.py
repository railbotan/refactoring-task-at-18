import numpy as np
from PIL import Image


def img_to_nparr(path):
    return np.array(Image.open(path))


def save_img_from_nparr(img, name):
    Image.fromarray(img).save(name)


def create_pixel_art(img, size, grayscale):
    for x in range(0, len(img), size):
        for y in range(0, len(img[1]), size):
            brightness = get_average_brightness(img, size, x, y)
            img[x: x + size, y: y + size] = brightness - brightness % grayscale
    return img


def get_average_brightness(img, size, x, y):
    return np.average(img[x: x + size, y: y + size])


img = img_to_nparr("img2.jpg")
save_img_from_nparr(create_pixel_art(img, 10, 50), 'res.jpg')
