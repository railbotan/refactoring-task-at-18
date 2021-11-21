from PIL import Image
import numpy as np

def get_brightness(arr_pixels, pix_x, pix_y, size_moz):
    sum_color = np.sum(arr_pixels[pix_x: pix_x + size_moz, pix_y: pix_y + size_moz])
    return int(sum_color // 3 // size_moz ** 2)

def set_color(arr_pixels, brightness, size_moz, pix_x, pix_y, step):
    value_grey = int(brightness // step) * step
    arr_pixels[pix_x: pix_x + size_moz, pix_y: pix_y + size_moz] = value_grey

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
