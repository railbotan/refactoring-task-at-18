from PIL import Image
import numpy as np
img = Image.open(input())
pixels = np.array(img)

def get_gray(pix_width, pix_height, x, y):
    result = 0
    for width in range(pix_width, pix_width + x):
        for height in range(pix_height, pix_height + y):
            color_1 = int(pixels[width][height][0])
            color_2 = int(pixels[width][height][1])
            color_3 = int(pixels[width][height][2])
            result += (color_1 + color_2 + color_3) / 3
    result = int(result // (x * y))
    return result


def replace_pixels(pix_width, x, pix_height, y, step_gray):
    gray = get_gray(pix_width, pix_height, x, y)
    for width in range(pix_width, pix_width + x):
        for height in range(pix_height, pix_height + y):
            pixels[width][height][0] = int(gray // step_gray) * step_gray
            pixels[width][height][1] = int(gray // step_gray) * step_gray
            pixels[width][height][2] = int(gray // step_gray) * step_gray


def get_gray_img(x, y, step_gray):
    height = len(pixels)
    width = len(pixels[1])
    pix_width = 0
    while pix_width < height:
        pix_height = 0
        while pix_height < width:
            replace_pixels(pix_width, x, pix_height, y, step_gray)
            pixels_y = pix_height + y
        pix_width = pix_width + x
    return pixels

mozaik = input(('Enter width, height, gray step')).split()
name = input(('Enter name of the result file')) + '.jpg'

Image.fromarray(get_gray_img(int(mozaik[0]), int(mozaik[1]), int(mozaik[2]))).save(name)
