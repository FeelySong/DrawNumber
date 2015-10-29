# coding=gb2312

from ghost import Ghost
import time
import lxml.html
ss=0
ghost = Ghost()
url="http://caipiao.163.com/order/cqssc/"
with ghost.start(download_images=False) as session:
    session.wait_timeout=60
    while ss<10:
        page, resources = session.open(url,timeout=60)
        html = lxml.html.fromstring(session.content)
        e=html.xpath(u'/html/body/article/section/aside/div[1]/div[1]/p[1]/strong/text()')
        print ''.join(e)
        num1=''.join(html.xpath(u'/html/body/article/section/aside/div[1]/div[1]/p[2]/em[1]/text()'))
        print num1
        ss=ss+1
        time.sleep(60)
    session.exit()