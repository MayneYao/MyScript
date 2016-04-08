from PIL import Image,ImageDraw,ImageFont

#设置字体及字号
font = ImageFont.truetype('simhei.ttf', 100)

for i in range(32,127):
    #打开空白图片100px
    img=Image.open("font.bmp")
    draw = ImageDraw.Draw(img)
    url = "ascll\\"+str(i)+".bmp"
    #参数（起始像素，字符，颜色，字体（字体+字号））
    draw.text((25,0), chr(i), fill=(0,0,0), font=font)
    img.save(url)


# def getImgpix (img):
#     width = img.size[0]
#     height = img.size[1]
#     for x in width:
#          for y in height:
#              r,g,b = img.getpixel((x,y))
#              _,*Gray=(r*30+g*59+b*11+50)/100