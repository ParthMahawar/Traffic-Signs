from pickle import load
from sys import argv
from PIL import Image

model = load(open("C:/users/Parth/desktop/save.dat", "rb"))
path = argv[1]

img = Image.open(path)
img = [list(img.getdata())]

print(model.predict(img))