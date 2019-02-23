# 电影天堂爬虫实战
# 目标：2019年新片精品前7页，每一部电影的详细内容
# 提取步骤：1.前7页的url  2.每部电影的url

from lxml import etree
import requests

BASE_DOMAIN = 'https://www.dytt8.net/'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
page_url = 'https://www.dytt8.net/html/gndy/dyzz/index.html'

def get_detail_urls(url):
    # 1.请求目标网站HTML文件
    response = requests.get(page_url,headers=HEADERS)
    text = response.text

    # 2.使用etree生成html对象
    html = etree.HTML(text)

    # 3.使用xpath语法解析数据
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    # movie字典保存对应信息
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imags = zoomE.xpath(".//img/@src")
    cover = imags[0]
    screenshot = imags[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    infos = zoomE.xpath(".//text()")
    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['address'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['grade'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['minutes'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("◎"):
                    break

    downloadurl = zoomE.xpath(".//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['downloadurl'] = downloadurl
    return movie

def spider():
    page_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    # 遍历7页网页
    for x in range(1,8):
        url = page_url.format(x)
        detail_urls = get_detail_urls(url)
        # 遍历电影详情介绍页面
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)

if __name__ == '__main__':
    spider()