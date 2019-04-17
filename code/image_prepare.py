from PIL import Image
import os
import numpy as np

def getimgvalues(folder, num):
    vals = []
    files = os.listdir(folder)
    counter = 0
    for file in files:
        try:
            img = Image.open(folder + file)
            vals.append(list(img.getdata()))
        except Exception as e: print(e)
        counter += 1
        if counter == num: break
    return np.array(vals)

if __name__ == "__main__":
    path = "C:/users/parth/desktop/Std_Train/40/300.png"
    img  = Image.open(path)
    print(list(img.getdata()))