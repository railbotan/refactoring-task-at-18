import numpy as np
from PIL import Image

def calc_gray(pix_x, pix_y, size, pix):
    res = np.sum((pix[pix_x: pix_x + size, pix_y: pix_y + size]) / 3)
    res = int(res // (size * size))
    return res

def change_pix(pix_x, pix_y, size, step, pix):
    gray = calc_gray(pix_x , size, pix_y, size, pix)
    pix[pix_x: pix_x + size, pix_y: pix_y + size] = int(gray // step) * step

def transform_img(pix, size,  grey_step):
    height = len(pix)
    width = len(pix[1])
    pix_x = 0
    step = 255 // (grey_step - 1)
    while pix_x < height:
        pix_y = 0
        while pix_y < width:
            change_pix(pix, pix_x, size, pix_y, size, step)
            pix_y = pix_y + size
        pix_x = pix_x + size
    return pix

img = Image.open(input('Введите имя входного файла: '))
size_pixel = int(input('Введите размер пикселя: '))
step_gray = int(input('Введите количество градаций: '))
res_file = input('Введите имя для сохранения: ')
pixels_img = np.array(img)
res = Image.fromarray(transform_img(pixels_img, size_pixel, step_gray))
res.save(res_file)