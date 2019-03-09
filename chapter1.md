# Scrapy笔记

### 创建项目和爬虫

* 创建项目

```
scrapy startproject [项目名称]
```

* 创建爬虫

到项目目录下

```
scrapy genspider [爬虫名字][目标网页的域名]
```

### 项目目录结构

1. items.py:用来存放爬虫爬取下来的数据模型。
2. middlewares.py:用来存放各种中间文件。
3. piplines.py:用来将items的模型存储到本地磁盘中。
4. settings.py:爬虫的信息配置（例如请求头、ip代理池等）
5. scrapy.py:项目的配置文件。
6. spider包:所有的爬虫都放在里面。

## 糗事百科Scrapy笔记

1.response可以执行xpath语法

2.提取出来的数据，是一个’Selector‘或者是一个'SelectorList'对象，获取其中字符串使用getall方法或者get方法

> getall        获取Selector中的所有文本，返回的是一个列表
>
> get            获取Selector中的第一个文本，返回的是一个string类型

3.数据传回来需要交给pipline处理，可以使用yield或者return列表（收集了所有item的列表）。

4.item：建议在'item.py'中定义好模型,以后就不使用字典。

```py
class CsbkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
```

5.pipline：这个是专门用来保存数据的,其中有三个方法会经常使用：

需要在settings.py中，设置’ITEM\_PIPLINE‘

* open\_spider\(self,spider\)      当爬虫被打开的时候执行
* process\_item（self,item,spider\)   当爬虫有item传过来的时候会被调用
* close\_spider\(self,spider\)   当爬虫被关闭的时候会被调用



