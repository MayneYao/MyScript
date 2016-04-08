from PIL import Image
img = Image.open("img/lod.png").convert("L")
img.show()