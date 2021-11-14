from PIL import Image
import numpy as np
imgName = input('Введите название исходного изображения (с расширением): ')
resName = input('Введите название конечного изображения (с расширением): ')
img = Image.open(imgName)
imgArray = np.array(img)
imgArrayLen = len(imgArray)
innerArrayLen = len(imgArray[1])
arrCounter = 0
size = int(input('Введите размер мозаики: '))
step = int(input('Введите количество градаций серого цвета: '))

def CountTotalSum(innerArrCounter, arrCounter):
    totalSum = 0
    tempArr = imgArray // 3
    for ac in range(arrCounter, arrCounter + size):
        for iac in range(innerArrCounter, innerArrCounter + size):
            totalSum += sum(tempArr[ac][iac])
    return int(totalSum // 100)

def CreatePixels(innerArrCounter, arrCounter, totalSum):
    for ac in range(arrCounter, arrCounter + size):
        for iac in range(innerArrCounter, innerArrCounter + size):
            imgArray[ac][iac][:] = int(totalSum // step) * step

while arrCounter < imgArrayLen - (size + 1):
    innerArrCounter = 0
    while innerArrCounter < innerArrayLen - (size + 1):
        totalSum = CountTotalSum(innerArrCounter, arrCounter)
        CreatePixels(innerArrCounter, arrCounter, totalSum)
        innerArrCounter = innerArrCounter + size - 1
    arrCounter = arrCounter + size - 1
res = Image.fromarray(imgArray)
res.save(resName)
print('Преобразование завершено!')
