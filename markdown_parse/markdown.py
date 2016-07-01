import re
import sys

re_lists_ul = '((\s+([\+\-\*])(\s+)([\w\d\u0391-\uFFE5]+))+)'
re_list_ul = "(\s+([\+\-\*])(\s+)([\w\d\u0391-\uFFE5]+))"
re_lists_ol = '((\s+(\d+\.)(\s+)([\w\d\u0391-\uFFE5]+))+)'
re_list_ol = "(\s+(\d+\.)(\s+)([\w\d\u0391-\uFFE5]+))"
re_h = '(?P<h_class>#{1,6})(?P<space>\s+)(?P<h_content>[\w\d\u0391-\uFFE5]+)'
re_h2 = '(?P<h>[\w\u0391-\uFFE5]+)(\n-+)'
re_block = '(\s> ((?P<quote>[\w\d\s\u0391-\uFFE5]+)+))'
re_img = '(!\[([\w\d\s\u0391-\uFFE5]+)\]\((((f|ht){1}(tp|tps)://)[-a-zA-Z0-9@:%_\+.~#?&//=]+)\))'
re_link = '([^!]\[([\w\d\s\u0391-\uFFE5]+)\]\((((f|ht){1}(tp|tps)://)[-a-zA-Z0-9@:%_\+.~#?&//=]+)\))'
re_code= '(`+?[\w]+([\w\W]+?)`+)'

def md2html_code(md):
    allcode = re.findall(re_code,md)
    for code in allcode:
        oldstr = code[0]
        codestr = code[1]
        newstr = "<code><pre>{codestr}</pre></code>".format(codestr=codestr)
        md = md.replace(oldstr,newstr)
    return md

def md2html_link(md):
    alllink = re.findall(re_link,md)
    for link in alllink:
        oldstr =link[0]
        txt = link[1]
        url =link[2]
        newstr = "<a href='{url}'>{txt}</a>".format(url=url,txt=txt)
        md = md.replace(oldstr,newstr)
    return md

def md2html_img(md):
    allimg = re.findall(re_img,md)
    for img in allimg:
        oldstr =img[0]
        txt = img[1]
        url =img[2]
        newstr = "<img src='{url}' alt='{txt}' />".format(url=url,txt=txt)
        md = md.replace(oldstr,newstr)
    return md

def md2html_block(md):
    m = re.findall(re_block,md)
    for i in m:
        oldstr = i[0]
        content = i[1]
        newstr = "<blockquote>{content}</blockquote>".format(content=content)
        md = md.replace(oldstr,newstr)
    return md

def md2html_list(md,type="default"):
    if type =="ul":
        re_lists = re_lists_ul
        re_list = re_list_ul
    elif type=="ol":
        re_lists = re_lists_ol
        re_list = re_list_ol
    else:
        return  "类型错误"
    all_list = re.findall(re_lists,md)
    for mylist in all_list:
        oldstr = mylist[0]
        newstr = oldstr
        lists = re.findall(re_list,oldstr)
        for li in lists:
            old = li[0]
            newstr = newstr.replace(old,"\n<li>{0}</li>".format(li[3]))
        newstr = "\n<{type}>{newstr}\n</{type}>\n".format(type=type,newstr=newstr)
        md = md.replace(oldstr,newstr)
    return md

def md2html_h(md):
    ##处理标题——横线
    m = re.findall(re_h2,md)
    for i in m:
        md = md.replace(i[0]+i[1],"<h2>"+i[0]+"</h2>\n")
    ##处理标题——井号
    m=re.findall(re_h,md)
    for h in m:
        oldstr = h[0]+h[1]+h[2]
        h_class=len(h[0])
        content = h[2]
        hh = "<h{h_class}>{content}</h{h_class}>".format(h_class=h_class,content=content)
        md = md.replace(oldstr,hh)
    return md


if __name__=="__main__":
    filename = sys.argv[-1]
    print(filename)
    with open(filename,'r',encoding='utf-8') as f:
        md = f.read()
        md = md2html_h(md)
        md = md2html_block(md)
        md = md2html_list(md,"ul")
        md = md2html_list(md,"ol")
        md = md2html_img(md)
        md = md2html_link(md)
        md = md2html_code(md)
        with open(filename[0:-3]+".html",'w',encoding='utf-8') as f:
             f.write(md)
        print("done")