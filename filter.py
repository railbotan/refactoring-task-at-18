import numpy as np
from PIL import Image

def calc_gray(pix_x, pix_y, size_x, size_y, pix):
    res = np.sum((pix[pix_x: pix_x + size_x, pix_y: pix_y + size_y]) / 3)
    res = int(res // (size_x * size_y))
    return res

def change_pix(pix_x, size_x, pix_y, size_y, step, pix):
    gray = calc_gray(pix_x , size_x, pix_y, size_y, pix)
    pix[pix_x: pix_x + size_x, pix_y: pix_y + size_y] = int(gray // step) * step

def transform_img(pix, size_x, size_y, grey_step):
    height = len(pix)
    width = len(pix[1])
    pix_x = 0
    step = 255 // (grey_step - 1)
    while pix_x < height:
        pix_y = 0
        while pix_y < width:
            change_pix(pix, pix_x, size_x, pix_y, size_y, step)
            pix_y = pix_y + size_y
        pix_x = pix_x + size_x
    return pix

img = Image.open("img2.jpg")
pixels_img = np.array(img)
res = Image.fromarray(transform_img(pixels_img, 10, 10, 5))
res.save('res.jpg')