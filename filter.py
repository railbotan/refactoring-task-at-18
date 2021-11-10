import numpy as np
from PIL import Image


def find_step(n):
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1))


def find_av_brightness(i, j, arr, m_h, m_w, step):
    br = 0
    for h in range(i, i + m_h):
        for w in range(j, j + m_w):
            r = int(arr[h][w][0])
            g = int(arr[h][w][1])
            b = int(arr[h][w][2])
            br += (r + g + b) / 3
    br //= m_h * m_w
    br -= br % step
    return br


def do_mosaic(arr, m_h, m_w, step):
    height = len(arr)
    width = len(arr[1])
    for i in range(0, height, m_h):
        for j in range(0, width, m_w):
            brightness = find_av_brightness(i, j, arr, m_h, m_w, step)
            for h in range(i, i + m_h):
                for w in range(j, j + m_w):
                    arr[h][w][0] = brightness
                    arr[h][w][1] = brightness
                    arr[h][w][2] = brightness


inp_im = np.array(Image.open("img2.jpg"))
inp_sizes = input('Enter the height and width of the mosaic element '
                  'separated by comma (for example: 10,10): ')
num_grad = int(input('Enter the number of gradations: '))

e_h, e_w = map(int, inp_sizes.split(','))
do_mosaic(inp_im, e_h, e_w, find_step(num_grad))

res = Image.fromarray(inp_im)
res.save("res.jpg")
