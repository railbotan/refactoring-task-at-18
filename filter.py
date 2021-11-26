from PIL import Image
import numpy as np
img = Image.open("img2.jpg")

def get_illumination(pixels, p_x, p_y, size):
    result = 0
    for range1 in range(p_x, p_x + size):
        for pillar in range(p_y, p_y + size):
            color_1 = int(pix[pillar][range1][0])
            color_2 = int(pix[pillar][range1][1])
            color_3 = int(pix[pillar][range1][2])
            summa = color_1 + color_2 + color_3
            result += int(summa // 3)
    result = int(result // (size * size))
    return result

def install_color(pixels, illumination, size, p_x, p_y, step):
    for range1 in range(p_x, p_x + size):
        for pillar in range(p_y, p_y + size):
            pixels[range1][pillar][0] = int(illumination // step) * step
            pixels[range1][pillar][1] = int(illumination // step) * step
            pixels[range1][pillar][2] = int(illumination // step) * step

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

res = Image.fromarray(grey_img(img, 10, 50))
res.save('res.jpg')
