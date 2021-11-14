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
    listImg = np.array(Image.open(img)).astype(int)
    limit = 255 // grad    
    lenImg = len(listImg)
    height = len(listImg[0])
    i = 0
    
    while i < lenImg:
        j = 0
        while j < height:
            part = listImg[i: size + i, j: size + j]
            sum = np.sum(part)
            avg = int(sum // (size ** 2))
            MakeColor(int(avg // limit) * limit / 3, listImg, size, i, j)
            j += size
        i += size
    
    return Image.fromarray(np.uint8(listImg))


CreateMosaicIMG(input("Enter the name of the image file: "),
            int(input("Enter the size of the mosaic: ")),
            int(input("Enter the size of the gradation: "))).save('res.jpg')
