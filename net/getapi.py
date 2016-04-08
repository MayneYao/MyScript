import requests
import re
import traceback
import time

baseUrl = "https://api.guildwars2.com/v2/items/"
zh = "?lang=zh"
en = "?lang=en"

def getItems():
    re = requests.get(baseUrl).json()
    return re

def getItemsDetail(id):
    en_item = requests.get(baseUrl+id+en).json()
    zh_item = requests.get(baseUrl+id+zh).json()
    en_name = en_item["name"]
    zh_name = zh_item["name"]
    description = zh_item.setdefault("description","暂无")
    type = zh_item["type"]
    detail = {"原名":en_name,"译名":zh_name,"描述":description,"类型":type}
    return detail

def detail2wiki():
    for i in range(len(ids)):
        ii = str(i//len(ids)*100)
        str1 = "现在进行到---------------"+ii+"%("+str(i)+")\n"
        print(str1)
        try:
            detail = getItemsDetail(ids[len(ids)-i-1])
            strx = "\n|-\n|"+detail["原名"]+"\n|[["+detail["译名"]+"]]\n|"+detail["描述"]+"\n|"+detail["类型"]
            if (not re.match("^\w{1,}",detail["原名"],re.I)):
                with open("wikitab_other.txt","a") as f:
                    f.write(strx)
                print("ID号:"+ids[len(ids)-i-1]+"-----"+detail["译名"])
            else:
                for x in a_z:
                    if (re.match("^"+x+"\w{1,}",detail["原名"],re.I)):
                        with open("wikitab_"+str(x)+".txt","a") as f:
                            f.write(strx)
                        print("ID号:"+ids[len(ids)-i-1]+"-----"+detail["译名"])
        except:
            with open("log.txt","a") as f:
                f.write("第"+ii+"项发生错误---------ID号:"+ids[len(ids)-i-1]+"\n__________________________________________________\n")
                traceback.print_exc(file=f)
                print("发生错误\n")
        finally:
            with open("undo_ids.txt","a") as f:
                f.write(ids[len(ids)-i-1]+", ")
            ids.pop()
            time.sleep(15)
def lista_z():
    a_z=[]
    for i in range(26):
        a_z.append(chr(i+ord("a")))
    return a_z



if __name__ == '__main__':
    with open("a.txt","r") as f:
        ids = f.read()
        ids = ids.split(", ")
    with open("undo_ids.txt","w") as f:
        f.write("-----------获取失败的id------------\n")
    with open("log.txt","w") as f:
        f.write("__________________log_____________\n")
    with open("wikitab_other.txt","w") as f:
        f.write('{| class="wikitable"\n!原名\n!译名\n!描述\n!类型\n')

    a_z = lista_z()

    for x in a_z:
        with open("wikitab_"+x+".txt","w") as f:
            f.write('{| class="wikitable"\n!原名\n!译名\n!描述\n!类型\n')
    detail2wiki()
    for x in a_z:
        with open("wikitab_"+x+".txt","a") as f:
            f.write("\n|}")