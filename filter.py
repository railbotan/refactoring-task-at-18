from PIL import Image
import numpy as np

def get_grey(s0, i, j):
    for n in range(i, i + mosaic_size):
        for k in range(j, j + mosaic_size):
            size[n][k][0] = int(s0 // grayscale) * grayscale
            size[n][k][1] = int(s0 // grayscale) * grayscale
            size[n][k][2] = int(s0 // grayscale) * grayscale
def get_px(i, j):
    s0 = 0
    for n in range(i, i + mosaic_size):
        for k in range(j, j + mosaic_size):
            a = int(size[n][k][0])
            b = int(size[n][k][1])
            c = int(size[n][k][2])
            s0 += (a + b + c) // 3
    return s0

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
