from PIL import Image

def img2ascll(url):
    img= Image.open(url).convert("L")
    #16阶灰度对应字符
    ascll=["M","W","N","B","R","G","E","@","F","*","[","v","(","\\","~","'"]
    width = img.size[0]
    height = img.size[1]
    #图片尺寸处理
    if(width>470):
        times = width/470
        w = 470
        h = int(height/times/2)
        img = img.resize((w,h),Image.ANTIALIAS)
        width = img.size[0]
        height = img.size[1]
    else:
        img = img.resize((width,height//2),Image.ANTIALIAS)
        height = img.size[1]
    #print(width,height)
    for i in range(0,height):
        for j in range(0,width):
            x= img.getpixel((j,i))
            x=x//16
            with open(url+".txt",'a') as f:
                if (j==width-1):
                    print("\n",file=f,end="")
                else:
                    print(ascll[x],file=f,end="")

img2ascll("t1.jpg")
