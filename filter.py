from PIL import Image
import numpy as np


def count_gray(pixels_x, pixels_y, size_x, size_y):
    gray = np.sum((pixels[pixels_x: pixels_x + size_x, pixels_y: pixels_y + size_y]) / 3)
    return int(gray // (size_x * size_y))


def replace_pixels(pixels_x, size_x, pixels_y, size_y, step):
    gray = count_gray(pixels_x, pixels_y, size_x, size_y)
    pixels[pixels_x: pixels_x + size_x, pixels_y: pixels_y + size_y] = int(gray // step) * step


def convert_gray_img(size_x, size_y, step):
    height = len(pixels)
    width = len(pixels[1])
    pixels_x = 0
    while pixels_x < height:
        pixels_y = 0
        while pixels_y < width:
            replace_pixels(pixels_x, size_x, pixels_y, size_y, step)
            pixels_y = pixels_y + size_y
        pixels_x = pixels_x + size_x
    return pixels


img = Image.open(input())
res_file = input()
pixels = np.array(img)
res = Image.fromarray(convert_gray_img(10, 10, 50))
res.save(res_file)



