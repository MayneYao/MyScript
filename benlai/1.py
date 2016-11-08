import requests
import logging

logging.basicConfig(filename="log.txt",level=logging.ERROR)

def get_items_by_page(page=1):
    """
    :param page:
    :return :
    """
    pdata = {
        "Page":str(page),
        "filter":".",
        "c1":"",
        "c2":"",
        "c3":"",
        "sort":0
    }
    re = requests.post("https://www.benlai.com/NewCategory/GetLuceneProduct",data=pdata).json()
    items_info ={"current_page":re["SelectNum"],"total_page":re["TotalNum"],"items":re["ProductList"]}
    return items_info

def save_img(name,img_url):
    name = name.replace('/','／') .replace('\\','＼').replace('"',"'").replace("*","x")
    img_name ="img\\{0}.jpg".format(name)
    with open(img_name,'wb') as f:
        f.write(requests.get(img_url).content)

if __name__ == "__main__":
    items_info = get_items_by_page()
    #items = items_info["items"]
    #cpage = items_info["current_page"]
    tpage = items_info["total_page"]
    for p in range(1,tpage+1):
        print("==正在进行第{0}页的商品收集==".format(p))
        items_info = get_items_by_page(p)
        items = items_info["items"]
        for item in items:
            try:
                item_name = item["ProductName"]
                print(item_name)
                item_img_url = item["ProductImageLink"]
                save_img(item_name,item_img_url)
            except:
                logging.error("未保存商品：{0} ".format(item_name))
                continue
