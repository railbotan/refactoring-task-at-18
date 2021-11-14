from PIL import Image
import numpy as np

def Get_gray_sum (arr, i, j, slice):
    gray_sum = 0
    for x in range(i, i + slice):
        for y in range(j, j + slice):
            red = arr[x][y][0]
            green = arr[x][y][1]
            blue = arr[x][y][2]
            middle_pixel = (int(red) + int(green) + int(blue)) / 3
            gray_sum += middle_pixel
    gray_sum = int(gray_sum // slice**2)
    return gray_sum

def Create_color (arr, i, j, gray_sum, slice, step):
    for x in range(i, i + slice):
        for y in range(j, j + slice):
            for z in range (3):
                arr[x][y][z] = int(gray_sum // step) * step

img = Image.open("img2.jpg")
arr = np.array(img)
pixels_count = len(arr)
width = len(arr[1])
i = 0
while i < pixels_count - 9:
    j = 0
    while j < width - 9:
        gray_sum = Get_gray_sum (arr, i, j, 10)
        Create_color(arr, i, j, gray_sum, 10, 50)
        j += 10
    i += 10
res = Image.fromarray(arr)
res.save('res.jpg')


