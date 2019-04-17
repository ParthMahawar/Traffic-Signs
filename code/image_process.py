from PIL import Image
import os
import numpy as np

def process(path, left, top, right, bottom):
    img = Image.open(path)
    img = img.crop((left, top, right, bottom))
    img = img.convert('L')
    img = img.resize((40, 40))
    return img

read_path = "C:/users/parth/desktop/GTSRB-Train/Final_Training/Images/"
write_path = "C:/users/parth/desktop/Std_Train/"

folders = [str(x).zfill(5) for x in range(43)]

for folder in folders:
    folder_path = read_path+folder+"/"
    save_path = write_path + str(int(folder)) + "/"
    details = open(folder_path + "GT-"+folder+".csv", "r")
    details = details.read().split("\n")[1:-1]

    for i in range(len(details)):
        details[i] = details[i].split(";")

    details = np.array(details)

    counter = 0

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    for detail in details:
        img = process(folder_path + detail[0], int(detail[3]), int(detail[4]), int(detail[5]), int(detail[6]))
        img.save(save_path + str(counter) + ".png")
        counter += 1