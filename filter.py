from PIL import Image
import numpy as np

def get_brightness(arr_pixels, pix_x, pix_y, size_moz):
    result_grey = 0
    for row in range(pix_x, pix_x + size_moz):
            for column in range(pix_y, pix_y + size_moz):
                first_color = arr_pix[row][column][0]
                second_color = arr_pix[row][column][1]
                third_color = arr_pix[row][column][2]
                sum_color = int(first_color) + int(second_color) + int(third_color)
                result_grey += int(sum_color // 3 // size_moz ** 2)
    return result_grey

def set_color(arr_pixels, brightness, size_moz, pix_x, pix_y, step):
    value_grey = int(brightness // step) * step
    for row in range(pix_x, pix_x + size_moz):
            for column in range(pix_y, pix_y + size_moz):
                arr_pixels[row][column][0] = value_grey
                arr_pixels[row][column][1] = value_grey
                arr_pixels[row][column][2] = value_grey

def grey_img(file_image, gradation, size_moz):
    arr_pixels = np.array(img)
    height = len(arr_pixels)
    width = len(arr_pixels[1])
    step = 255 // graduation
    for y in range(0, height, size_moz):
        for x in range(0, width, size_moz):
             brightness = get_brightness(arr_pixels, pix_x, pix_y, size_moz)
             set_color(arr_pixels, brightness, size_moz, pix_x, pix_y, step)
    return arr_pixels

img = Image.open("img2.jpg")
res = Image.fromarray(grey_img(img, 10, 50))
res.save('res.jpg')
