from pickle import load
import numpy as np
from PIL import Image

path  = "C:/users/parth/desktop/Std_Test/"
model = load(open("C:/users/parth/desktop/save.dat","rb"))
details = open(path+"GT-Final_Test.csv").read()
details = np.array([detail.split(';') for detail in details.split("\n")][1:-1])[:,[0,-1]]

correct = 0
wrong = 0

for detail in details:
    cls = int(detail[1])
    img = Image.open(path+detail[0])
    img = [list(img.getdata())]

    prediction = model.predict(img)
    if prediction == cls: correct+=1
    else: wrong += 1

    print(correct, wrong)
    print("Accuracy", 100*(correct/(correct+wrong)))