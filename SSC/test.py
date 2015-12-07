# coding=gb2312

from ghost import Ghost
import time
import lxml.html
ss=0
ghost = Ghost()
url="http://baidu.lecai.com/lottery/draw/view/557/"
with ghost.start(download_images=False) as session:
    session.wait_timeout=60
    while ss<10:
        page, resources = session.open(url,timeout=60)
        html = lxml.html.fromstring(session.content)
        e=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/h1/b/text()')
        print ''.join(e)
        n1=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[1]/text()')
        n2=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[2]/text()')
        n3=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[3]/text()')
        n4=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[4]/text()')
        n5=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[5]/text()')
        n6=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[6]/text()')
        n7=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[7]/text()')
        n8=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[8]/text()')
        n9=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[9]/text()')
        n10=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/div[1]/label/span[10]/text()')
        draw_code=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
        print type(draw_code)
        time.sleep(60)
        ss=ss+1
    session.exit()