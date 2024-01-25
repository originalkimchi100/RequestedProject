# -*- coding:utf-8 -*-

import pylab as P
import numpy as N
import cv2
import os
from PIL import Image

sample = cv2.imread('sample/Test.jpg', cv2.IMREAD_GRAYSCALE)
sample = sample.astype(float)


print(sample.shape)

ErrorRange = {}



folder_path = "images"
file_list = os.listdir(folder_path)
print(file_list)
file_count = len(file_list)
print(file_count)


for file in file_list:
    img2 = cv2.imread(f"images/{file}", cv2.IMREAD_GRAYSCALE)
    img2 = img2.astype(float)

    result = img2 - sample
    result = N.square(result.tolist())
    result = N.sum(result.tolist(), axis = 1)
    result = N.sum(result)
    ErrorRange[file] = result

print(ErrorRange)

ErrorRange = sorted(ErrorRange.items(), key = (lambda x:x[1]))
print(ErrorRange)

first_key = list(ErrorRange[0])
second_key = list(ErrorRange[1])
third_key = list(ErrorRange[2])

print(f'첫번째 key : {first_key}')
print(f'두번째 key : {second_key}')
print(f'첫번째 key : {third_key}')

'''
print(min(ErrorRange))
print(ErrorRange.index(min(ErrorRange)))
print(f"최대 유사한 파일:{file_list[ErrorRange.index(min(ErrorRange))]}")
print(ErrorRange)
image = Image.open("images/" + file_list[ErrorRange.index(min(ErrorRange))])

image.show()
'''