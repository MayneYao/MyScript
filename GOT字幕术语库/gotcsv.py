import csv
import re


def addWord(en,zh,pos='',des='',note=''):
    with open('got1.0.csv','a',newline='',encoding='utf-8') as f:
        w =csv.writer(f,quoting=csv.QUOTE_ALL)
        w.writerow([en,zh,pos,des,note])

# def delWord(word):
#     with open('got1.0.csv','r+',newline='',encoding='utf-8') as f:
#         r = csv.reader(f, quoting=csv.QUOTE_NONE)
#
#         for i in r:
#             if re.search(word,i[0]+i[1]+i[2]+i[3]+i[4]):
#                 pass
#             else:
#                 #with open("text1.csv",'a',newline='',encoding='utf-8') as f1:
#                     #w = csv.writer(f1)
#                 #print(i)
#                 pass
#                     #w.writerow(i)
#         # for i in r:
#         #     print(re.search('Lord',i))
#         # #     print(','.join(i))


