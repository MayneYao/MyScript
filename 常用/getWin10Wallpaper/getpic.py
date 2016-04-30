import os
import shutil
import getpass
import re
import sys
from PIL import Image


def getWin10Pic2tmp():
    #path =path1+user+path2+path3=path4
    user=getpass.getuser()
    path1 = "C:\\Users\\"
    path2 = "\\AppData\\Local\\Packages\\"
    path3 = ""
    path4 = "\\LocalState\\Assets\\"
    apath = path1+user+path2

    for i in os.listdir(apath):
        if(re.match("Microsoft.Windows.ContentDeliveryManager",i)):
            path3=i

    topath = apath+path3+"\\LocalState\\getWin10Pic_tmp"

    if (os.path.exists(topath)):
        pass
    else:
        os.mkdir(topath)
    path = apath+path3+path4
    for i in os.listdir(path):
        fileSize = os.path.getsize(path+"\\"+i)
        oldfile = path+"\\"+i
        newfile = topath+"\\"+i+".jpg"
        #拷贝图片大小大于400k的图
        if (fileSize/1024>400):
           if os.path.isfile(newfile):
               pass
           else:
               shutil.copyfile(oldfile,newfile)
    return topath

def fromTmp2TargetPath():
    # *biu,topath= sys.argv
    # if(topath):
    #     print(topath)

    curpath = os.path.abspath(os.curdir)
    topath =curpath+"\\Win10Pic"
    if (os.path.exists(topath+"\\PC")):
        pass
    elif (os.path.exists(topath+"\\Phone")):
        pass
    else:
        os.makedirs(topath+"\\PC")
        os.makedirs(topath+"\\Phone")
    frompath =getWin10Pic2tmp()

    for i in os.listdir(frompath):
        oldFile = frompath+"\\"+i
        img = Image.open(oldFile)
        width = img.size[0]
        height = img.size[1]
        img.close()
        if (width==1080 and height==1920):
            newfile = topath+"\\Phone\\Phone_"+i
        elif (height==1080 and width==1920):
            newfile = topath+"\\PC\\Pc_"+i
        else:
            os.remove(oldFile)
        try:
            shutil.copyfile(oldFile,newfile)
        except:
            continue

if __name__=="__main__":
    fromTmp2TargetPath()
