from PIL import Image
import numpy as np

def get_grey(s0, i, j):
    size[i: i + mosaic_size, j: j + mosaic_size, 0] = int(s0 // grayscale) * grayscale
    size[i: i + mosaic_size, j: j + mosaic_size, 1] = int(s0 // grayscale) * grayscale
    size[i: i + mosaic_size, j: j + mosaic_size, 2] = int(s0 // grayscale) * grayscale
def get_px(i, j):
    return np.sum(size[i: i + mosaic_size, j: j + mosaic_size]) // 3

grayscale = int(input())
mosaic_size = int(input())

img = Image.open("img2.jpg")

size = np.array(img)
height = len(size)
width = len(size[1])

i = 0

while i < height:
    j = 0
    while j < width:
        s = int(get_px(i, j) // (mosaic_size * mosaic_size))
        get_grey(s, i, j)
        j = j + mosaic_size
    i = i + mosaic_size
res = Image.fromarray(size)
res.save('res.jpg')
