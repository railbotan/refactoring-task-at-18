import numpy as np
from PIL import Image


def find_step(n):
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1))


def find_av_brightness(i, j, arr, m_h, m_w, step):
    br = 0.
    br += arr[i: i + m_h, j: j + m_w, :].sum() / 3
    br //= m_h * m_w
    br -= br % step
    return np.uint8(br)


def do_mosaic(arr, m_h, m_w, step):
    for i in range(0, len(arr), m_h):
        for j in range(0, len(arr[1]), m_w):
            brightness = find_av_brightness(i, j, arr, m_h, m_w, step)
            arr[i: i + m_h, j: j + m_w, :] = brightness


inp_im = np.array(Image.open("img2.jpg"))
inp_sizes = input('Enter the height and width of the mosaic element '
                  'separated by comma (for example: 10,10): ')
num_grad = int(input('Enter the number of gradations: '))

e_h, e_w = map(int, inp_sizes.split(','))
do_mosaic(inp_im, e_h, e_w, find_step(num_grad))

res = Image.fromarray(inp_im)
res.save("res.jpg")
