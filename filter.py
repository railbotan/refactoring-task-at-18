from PIL import Image
import numpy as np


def count_gray(pixels, pixels_x, pixels_y, size_x, size_y):
    gray = 0
    for index_x in range(pixels_x, pixels_x + size_x):
        for index_y in range(pixels_y, pixels_y + size_y):
            color_1 = pixels[index_x][index_y][0]
            color_2 = pixels[index_x][index_y][1]
            color_3 = pixels[index_x][index_y][2]
            gray += (int(color_1) + int(color_2) + int(color_3)) / 3
    gray = int(gray // (size_x * size_y))
    return gray


def replace_pixels(pixels, pixels_x, size_x, pixels_y, size_y, step):
    gray = count_gray(pixels, pixels_x, pixels_y, size_x, size_y)
    for index_x in range(pixels_x, pixels_x + size_x):
        for index_y in range(pixels_y, pixels_y + size_y):
            pixels[index_x][index_y][0] = int(gray // step) * step
            pixels[index_x][index_y][1] = int(gray // step) * step
            pixels[index_x][index_y][2] = int(gray // step) * step


def convert_gray_img(pixels, size_x, size_y, grey_step):
    step = 255 // (grey_step - 1)
    height = len(pixels)
    width = len(pixels[1])
    pixels_x = 0
    while pixels_x < height:
        pixels_y = 0
        while pixels_y < width:
            replace_pixels(pixels, pixels_x, size_x, pixels_y, size_y, step)
            pixels_y = pixels_y + size_y
        pixels_x = pixels_x + size_x
    return pixels


img = Image.open("img2.jpg")
pixels_img = np.array(img)
res = Image.fromarray(convert_gray_img(pixels_img, 10, 10, 5))
res.save('res.jpg')
