from PIL import Image
import numpy as np

def Get_gray_sum (img_list, i, j, area):
    gray_sum = 0
    for x in range(i, i + area):
        for y in range(j, j + area):
            red = img_list[x][y][0]
            green = img_list[x][y][1]
            blue = img_list[x][y][2]
            middle_pixel = (int(red) + int(green) + int(blue)) / 3
            gray_sum += middle_pixel
    gray_sum = int(gray_sum // area**2)
    return gray_sum

def Create_color (img_list, i, j, gray_sum, area, step):
    for x in range(i, i + area):
        for y in range(j, j + area):
            for z in range (3):
                img_list[x][y][z] = int(gray_sum // step) * step

img_list = np.array(Image.open("img2.jpg"))
pixels_count = len(img_list)
width = len(img_list[1])
i = 0
while i < pixels_count - 9:
    j = 0
    while j < width - 9:
        gray_sum = Get_gray_sum (img_list, i, j, 10)
        Create_color(img_list, i, j, gray_sum, 10, 6)
        j += 10
    i += 10
Image.fromarray(img_list).save('res.jpg')