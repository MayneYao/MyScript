#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
import requests
import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import logging
#import mysql.connector
import time 

#日志信息设定
localtime = time.asctime(time.localtime(time.time()))
FileName = '/root/gw2/mail.log'
logging.basicConfig(filename=FileName,level=logging.DEBUG)
logging.debug('--------------------'+localtime+'---------------------')

anet ='https://www.guildwars2.com/en/feed/'
dulfy ='http://dulfy.net/category/gw2/feed/'
timetod =str(datetime.date.today())
loc_url_anet = '/root/gw2/gw2news/url_anet/'+timetod+'.txt'
loc_url_anet_old = '/root/gw2/gw2news/url_anet/'+timetod+'-old.txt'
loc_url_dulfy = '/root/gw2/gw2news/url_dulfy/'+timetod+'.txt'
loc_url_dulfy_old = '/root/gw2/gw2news/url_dulfy/'+timetod+'-old.txt'

url_new_list =[]
url_old_list =[]
url_list=[]
title_list=[]
content_list=[]
address=[]


#得到最新的url列表
def get_new_url(name):
    if name==anet:
        loc_url_ =loc_url_anet
    if name==dulfy:
        loc_url_ =loc_url_dulfy
    r =requests.get(name)
    r = r.text
    x = bs(r,'html.parser')
    link =x.find_all("link")
    x_url =[]
    for i in link:
        if i.get_text()=="http://dulfy.net" or i.get_text()=="https://www.guildwars2.com":
            pass
        else:
            x_url.append(i.get_text())
    for i in x_url:
        url_new_list.append(i)
    return url_new_list


#新的url列表同旧列表比较，返回flag，更新的列表url写入文件
def cmp_url(name):
    if name==anet:
        loc_url_ =loc_url_anet_old
    if name==dulfy:
        loc_url_ =loc_url_dulfy_old
    flag =0
    with open(loc_url_,'r') as oldf:
        url_old_list =oldf.read()
        url_old_list =url_old_list.split('\n')
        for i in url_new_list:
            if (i not in url_old_list):
                url_list.append(i)
                flag+=1
        with open(loc_url_,'w') as f:
                for j in url_new_list:
                    f.write(j+'\n')
    return flag

#获取更新的url的内容
def get_html(name):
    if name == anet:
        r =requests.get(name)
        r =r.text
        html = bs(r,'html.parser')
        title =html.find_all(("title"))
        text =html.find_all("content:encoded")
        for i in range(0,len(url_list)):
            with open('/root/gw2/gw2news/content_anet/'+title[i+1].string+'.html','wb') as f:
                f.write(text[i].encode('utf-8'))

    if name == dulfy:
        for i in url_list:
            r = requests.get(i)
            r =r.text
            html =bs(r,'html5lib')
            myt =html.find_all('h1',class_="post-title")
            myt =myt[0].string
            myt =myt.replace('/',' ')
            content =html.find_all("div",class_='post-content')
            meta =html.find_all("p",class_='post-meta')
            meta[0].clear()
            xxx =html.find_all('span',class_='author-avatar')
            xxxx=html.find_all('span',class_='author-name')
            xxx[0].clear()
            xxxx[0].clear()
            html.find_all('span','post-comment')[0].clear()
            share =html.find_all("div",class_='sharedaddy')
            share[0].clear()
            content =content[0]
            loc_content='/root/gw2/gw2news/content_dulfy/'+myt+'.html'
            with open(loc_content,'wb') as f:
                f.write(content.encode('utf-8'))
                content_list.append(loc_content)
                title_list.append(myt)

#从数据得到邮件列表地址,加入到要发送的邮件地址表中
def getaddress():
 #   con =mysql.connector.connect(user='root',password='mypwd',database='gw2')
 #  cursor =con.cursor()
 #   cursor.execute('select distinct * from email')
 #   v=cursor.fetchall()
 #   for i in v:
 #       address.append(i[0])
    address.append('250195058@qq.com')
    address.append('513358099@qq.com')
#邮件编码转换
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#发送邮件
def sendemail(sendhtml,title,to_addr):
    from_addr = 'kungenloveu@163.com'
    password = '###mypwd'
    smtp_server = 'smtp.163.com'

    msg = MIMEText(sendhtml, 'html', 'utf-8')
    msg['From'] = _format_addr('鲲艮喜欢你 <%s>' % from_addr)
    msg['To'] = _format_addr('Dear GW2er <%s>' % to_addr)
    msg['Subject'] = Header(title, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

#发送内容消息
def send():
    if flg ==0:
        print('no change,no send')
        logging.exception('no change,no send')
    elif flg<0:
        print("error")
        logging.exception('Error!')
    else:
        for i in range(0,flg):
            with open(content_list[i],'rb',) as f:
                sendhtml = f.read()
                tt = title_list[i]
                for a in address:
                     sendemail(sendhtml,tt,a)
                print('发送成功')
                logging.exception('successsss!')

if __name__ == '__main__':

    get_new_url(dulfy)
    flg =cmp_url(dulfy)
    get_html(dulfy)
    getaddress()
    send()
