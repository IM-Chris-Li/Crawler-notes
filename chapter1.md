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



