from PIL import Image
import numpy as np
img = Image.open(input("Введите название входного файла"))

def get_illumination(pixels, p_x, p_y, size):
    summa = np.sum(pixels[p_x: p_x + size, p_y: p_y + size])
    result = int(summa // 3)
    return int(result // (size * size))

def install_color(pixels, illumination, size, p_x, p_y, step):
    pixels[p_x: p_x + size, p_y: p_y + size] = int(illumination // step) * step

def get_gray(file_image, gradation, size):
    step = 255 // graduation
    pixels = np.array(img)
    hei = len(pixels)
    wid = len(pixels[1])
    for y in range(0, hei, size):
        for x in range(0, wid, size):
            illumination = get_illumination(pixels, p_x, p_y, size)
            install_color(pixels, illumination, size, p_x, p_y, step)
    return pixels

res = Image.fromarray(grey_img(input("Введите название входного файла"), 
                               int(input("Введите размер градации")), 
                               int(input("Введите размер мозаики"))))
res.save(input("Введите название для сохроняемого файла"))
