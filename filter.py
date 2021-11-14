from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
imgArray = np.array(img)
imgArrayLen = len(imgArray)
innerArrayLen = len(imgArray[1])
arrCounter = 0
size = int(input('Введите размер мозаики: '))
step = int(input('Введите количество градаций серого цвета: '))

def CountTotalSum(innerArrCounter, arrCounter):
    totalSum = 0
    for ac in range(arrCounter, arrCounter + size):
        for iac in range(innerArrCounter, innerArrCounter + size):
            firstElem = imgArray[ac][iac][0] // 3
            secondElem = imgArray[ac][iac][1] // 3
            thirdElem = imgArray[ac][iac][2] // 3
            elemSum = int(firstElem) + int(secondElem) + int(thirdElem)
            totalSum += elemSum
    return int(totalSum // 100)

def CreatePixels(innerArrCounter, arrCounter, totalSum):
    for ac in range(arrCounter, arrCounter + size):
        for iac in range(innerArrCounter, innerArrCounter + size):
            imgArray[ac][iac][0] = int(totalSum // step) * step
            imgArray[ac][iac][1] = int(totalSum // step) * step
            imgArray[ac][iac][2] = int(totalSum // step) * step

while arrCounter < imgArrayLen - (size + 1):
    innerArrCounter = 0
    while innerArrCounter < innerArrayLen - (size + 1):
        totalSum = CountTotalSum(innerArrCounter, arrCounter)
        CreatePixels(innerArrCounter, arrCounter, totalSum)
        innerArrCounter = innerArrCounter + size - 1
    arrCounter = arrCounter + size - 1
res = Image.fromarray(imgArray)
res.save('res.jpg')

