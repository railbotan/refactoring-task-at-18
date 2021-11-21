from PIL import Image
import numpy as np
img_name = input('Введите название исходного изображения (с расширением): ')
res_name = input('Введите название конечного изображения (с расширением): ')
img = Image.open(img_name)
img_array = np.array(img)
size = int(input('Введите размер мозаики: '))
step = int(input('Введите количество градаций серого цвета: '))
grad_step = 255 // step

def find_av_brightness(part_of_img, size, grad_step):
    total_sum = np.sum(part_of_img[:size, :size]) / 3
    av_brightness = total_sum // size * size
    return int(av_brightness // grad_step) * grad_step


def convert_to_grey_img(img_array, size, grad_step):
    for i in range(0, len(img_array), size):
        for j in range(0, len(img_array[0]), size):
            img_array[i:i + size, j:j + size] = find_av_brightness(img_array[i:i + size, j:j + size], size, grad_step)
    return img_array

res = Image.fromarray(convert_to_grey_img(img_array, size, grad_step))
res.save(res_name)
print('Преобразование завершено!')
