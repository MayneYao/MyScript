import my.myimg.img as img
import os

baseurl ="E:\\pycode\\img\\"

name="badman.jpg"
txt =baseurl+name+".txt"
file = baseurl+name

if(os.path.exists(txt)):
    os.remove(txt)

if(os.path.exists(file)):
    img.img2ascll(file)
else:
    print("file doesn't exist！（")
print("done")

