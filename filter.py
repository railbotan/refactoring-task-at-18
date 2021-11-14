from PIL import Image
import numpy as np


def MosaicSum(array, size, i, j):
    sum = 0
    
    for x in range(i, i + size):
        for y in range(j, j + size):
            redGrad = array[x][y][0]
            greenGrad = array[x][y][1]
            blueGrad = array[x][y][2]
            M = redGrad + greenGrad + blueGrad
            sum += M
    
    return sum


def MakeColor(newMatrix, matrix, size, i, j):
    for x in range(i, i + size):
        for y in range(j, j + size):
            for z in range(3):
                matrix[x][y][z] = newMatrix


def CreateMosaicIMG(img, size, grad):
    limit = 255 // grad
    listImg = np.array(img).astype(int)
    lenImg = len(listImg)
    height = len(listImg[0])
    i = 0
    
    while i < lenImg:
        j = 0
        while j < height:
            sum = MosaicSum(listImg, size, i, j)
            avg = int(sum // (size ** 2))
            MakeColor(int(avg // limit) * limit / 3, listImg, size, i, j)
            j += size
        i += size
    
    return Image.fromarray(np.uint8(listImg))


img = Image.open("img2.jpg")
resolution = CreateMosaicIMG(img, size = 15, grad = 5)
resolution.save('res.jpg')
