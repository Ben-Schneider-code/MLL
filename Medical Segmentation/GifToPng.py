from PIL import Image
from os import listdir
from os.path import isfile, join

path = "./data/training/target/"

files = [f for f in listdir(path) if isfile(join(path, f))]

print(files)

for file in files:
    img = Image.open(path + file)
    file = file.split(".")
    file = file[0] + ".png"
    print(file)
    img.save(file)
