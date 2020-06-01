#!/usr/bin/env python
#conding:utf8


import requests
from lxml import etree
import re
import time
from bs4 import BeautifulSoup as BS
import tomd
'''
url=https://cuiqingcai.com/page/24?s=%E7%88%AC%E8%99%AB
'''

header = {
    'Cookie': 'UM_distinctid=17081aec19d464-029f18b12feb2f-7a1437-144000-17081aec19fdb; PHPSESSID=39mvmlsqcbsudn5cl62gsupna4; Hm_lvt_3ef185224776ec2561c9f7066ead4f24=1586513113,1587912323; Hm_lpvt_3ef185224776ec2561c9f7066ead4f24=1587912346; CNZZDATA1253486800=2084679396-1582719716-https%253A%252F%252Fwww.baidu.com%252F%7C1587912349',
    'Referer': 'https://cuiqingcai.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

'''
['https://cuiqingcai.com/9075.html', 'https://cuiqingcai.com/9075.html', 'https://cuiqingcai.com/9075.html#comments', 'https://cuiqingcai.com/8703.html', 'https://cuiqingcai.com/8703.html', 'https://cuiqingcai.com/8703.html#comments', 'https://cuiqingcai.com/8678.html', 'https://cuiqingcai.com/8678.html', 'https://cuiqingcai.com/8678.html#comments', 'https://cuiqingcai.com/8648.html', 'https://cuiqingcai.com/8648.html', 'https://cuiqingcai.com/8648.html#comments', 'https://cuiqingcai.com/8627.html', 'https://cuiqingcai.com/8627.html', 'https://cuiqingcai.com/8627.html#comments', 'https://cuiqingcai.com/8509.html', 'https://cuiqingcai.com/8509.html', 'https://cuiqingcai.com/8509.html#comments', 'https://cuiqingcai.com/8506.html', 'https://cuiqingcai.com/8506.html', 'https://cuiqingcai.com/8506.html#respond', 'https://cuiqingcai.com/8494.html', 'https://cuiqingcai.com/8494.html', 'https://cuiqingcai.com/8494.html#comments', 'https://cuiqingcai.com/8491.html', 'https://cuiqingcai.com/8491.html', 'https://cuiqingcai.com/8491.html#comments', 'https://cuiqingcai.com/8475.html', 'https://cuiqingcai.com/8475.html', 'https://cuiqingcai.com/8475.html#respond', 'https://weibo.com/cuiqingcai', 'http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=cqc@cuiqingcai.com', '?feed=rss2', 'https://cuiqingcai.com/1052.html', 'https://cuiqingcai.com/4320.html', 'https://cuiqingcai.com/4352.html', 'http://www.9191boke.com/', 'https://www.3maio.com', 'https://diygod.me/', 'https://www.findhao.net', 'https://higuoxing.com', 'http://www.urselect.com/?aid=dnk9st', 'https://www.yuanrenxue.com/', 'http://www.lizenghai.com/', 'http://lanbing510.info', 'https://lengyue.me/', 'http://qianxunclub.com/', 'http://www.kunkundashen.cn/', 'http://www.hellobi.com/', 'http://www.cenchong.com/', 'https://upliu.net/', 'https://seofangfa.com', 'http://www.hubwiz.com', 'http://frankchen.xyz/', 'http://bysocket.com', 'http://zerlong.com/', 'https://www.binblogs.cn', 'http://ysir308.com/', 'http://ibloger.net', 'http://redstonewill.com/', 'http://www.laodong.me', 'http://www.lanqibing.com/', 'http://zhaoshuai.me/%20', 'https://cloud.tencent.com/', 'https://www.qiniu.com/']
['https://cuiqingcai.com/8394.html', 'https://cuiqingcai.com/8394.html', 'https://cuiqingcai.com/8394.html#comments', 'https://cuiqingcai.com/8385.html', 'https://cuiqingcai.com/8385.html', 'https://cuiqingcai.com/8385.html#respond', 'https://cuiqingcai.com/8381.html', 'https://cuiqingcai.com/8381.html', 'https://cuiqingcai.com/8381.html#respond', 'https://cuiqingcai.com/8364.html', 'https://cuiqingcai.com/8364.html', 'https://cuiqingcai.com/8364.html#respond', 'https://cuiqingcai.com/8361.html', 'https://cuiqingcai.com/8361.html', 'https://cuiqingcai.com/8361.html#respond', 'https://cuiqingcai.com/8353.html', 'https://cuiqingcai.com/8353.html', 'https://cuiqingcai.com/8353.html#respond', 'https://cuiqingcai.com/8350.html', 'https://cuiqingcai.com/8350.html', 'https://cuiqingcai.com/8350.html#respond', 'https://cuiqingcai.com/8337.html', 'https://cuiqingcai.com/8337.html', 'https://cuiqingcai.com/8337.html#comments', 'https://cuiqingcai.com/8333.html', 'https://cuiqingcai.com/8333.html', 'https://cuiqingcai.com/8333.html#comments', 'https://cuiqingcai.com/8320.html', 'https://cuiqingcai.com/8320.html', 'https://cuiqingcai.com/8320.html#comments', 'https://weibo.com/cuiqingcai', 'http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&email=cqc@cuiqingcai.com', '?feed=rss2', 'https://cuiqingcai.com/1052.html', 'https://cuiqingcai.com/4320.html', 'https://cuiqingcai.com/4352.html', 'http://www.9191boke.com/', 'https://www.3maio.com', 'https://diygod.me/', 'https://www.findhao.net', 'https://higuoxing.com', 'http://www.urselect.com/?aid=dnk9st', 'https://www.yuanrenxue.com/', 'http://www.lizenghai.com/', 'http://lanbing510.info', 'https://lengyue.me/', 'http://qianxunclub.com/', 'http://www.kunkundashen.cn/', 'http://www.hellobi.com/', 'http://www.cenchong.com/', 'https://upliu.net/', 'https://seofangfa.com', 'http://www.hubwiz.com', 'http://frankchen.xyz/', 'http://bysocket.com', 'http://zerlong.com/', 'https://www.binblogs.cn', 'http://ysir308.com/', 'http://ibloger.net', 'http://redstonewill.com/', 'http://www.laodong.me', 'http://www.lanqibing.com/', 'http://zhaoshuai.me/%20', 'https://cloud.tencent.com/', 'https://www.qiniu.com/']


'''

#获取链接
def get_url(url):

    time.sleep(1)
    res = requests.get(url,headers=header)
    html = etree.HTML(res.text)
    art_url = html.xpath('//a[@target="_blank"]/@href')
     #去重
    set_url = set()
    set_url = art_url[:30]
     # # print(arc_url)
     # #转化成列表
     # url_list = list(set_url)
     #从字典获取链接，进行截取，再次存入一个字典中（去重）
    s = set()
    for url in set_url:
        s.add(re.search('.*\.html',url).group())
    print(s)
    # print(s)
    #for循环获取文章详细界面
    for i in s:
        print('正在处理此链接%s' % i)
        get_art(i)
        print('处理完成')


def get_art(url):

    #url = 'https://cuiqingcai.com/8468.html'
    #time.sleep(1)
    print(url)
    res = requests.get(url, headers=header)
    time.sleep(1)
    html = etree.HTML(res.text)
    art_title = html.xpath('//h1[@class="article-title"]/a/text()')
    #art_content = html.xpath('//article[@class="article-content"]/p/text()')
    #p = re.compile('<article class="article-content">.*</article>')
    #art_content2 = p.search(res.text)
    #art_content2  = re.search('<article class="article-content">.*?</article>',res.text)
    soup = BS(res.text)
    content = soup.article
    #print(art_title)
    #print(res.text)
    #print(content)
    print('页面下载完毕，正在生成md文件')
    text = tomd.Tomd(str(content)).markdown
    print(art_title)
    #print(text)
    with open('./book/%s.md'%art_title,'w',encoding='utf-8') as f:
        f.write('#%s'%art_title)
        f.write(text)
    print('%s----markdown文件下载完毕'%art_title[0])



if __name__ == '__main__':
    for i in range(2,25):
        url = "https://cuiqingcai.com/page/%d?s=爬虫"%(i)
        get_url(url)
        #time.sleep()

