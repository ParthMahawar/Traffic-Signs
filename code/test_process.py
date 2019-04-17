import os
import numpy as np
from PIL import Image

def process(path, left, top, right, bottom):
    img = Image.open(path)
    img = img.crop((left, top, right, bottom))
    img = img.convert('L')
    img = img.resize((40, 40))
    return img

read_path = "C:/Users/Parth/Desktop/GTSRB-Test/Final_Test/Images/"
write_path = "C:/Users/Parth/Desktop/Std_test/"
details = open(read_path+"GT-final_test.csv", "r").read()

details = np.array([detail.split(';') for detail in details.split("\n")][1:-1])

for detail in details:
    name = detail[0][:-4]
    img = process(read_path + detail[0], int(detail[3]), int(detail[4]), int(detail[5]), int(detail[6]))
    img.save(write_path+name+".png")
