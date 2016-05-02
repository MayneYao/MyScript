csv（Comma-Separated Values，逗号分隔值）文件以纯文本的形式存储表格数据，广泛地应用于程序之间转移表格数据,是一种很简单的数据格式

GTT（Google Translator Toolkit ，谷歌译者工具包）术语库
------------------------------------------
GTT的字幕库要求是csv格式的，要求格式如下

以got的字幕库为例

第一行 要标明:原文语言，译文语言，词性（可选），说明（可选），备注（可选）
```
en,zh-Hans,pos,description,notes
```

python中操作csv
--------------
用csv模块即可方便的操作csv文件

读
``` python
import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        print(', '.join(row))
```

写
``` python
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
```

参数说明 

**delimiter**指定分隔符，默认为逗号

**quotchar**包含数据的符号,默认是双引号

**quoting**包含方式，参数如下

QUOTE_ALL
不管是什么类型, 任何内容都加上引号

QUOTE_MINIMAL
这是默认的, 使用指定的字符引用各个域(如果解析器被配置为相同的dialect和选项时, 可能会让解析器在解析时产生混淆)

QUOTE_NONNUMERIC
引用那些不是整数或浮点数的域. 当使用读取对象时, 如果输入的域是没有引号, 那么它们会被转换成浮点数.

QUOTE_NONE
对所有的输出内容都不加引用, 当使用读取对象时, 引用字符看作是包含在每个域的值里(但在正常情况下, 他们被当成定界符而被去掉)

