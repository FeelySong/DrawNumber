# coding=gb2312

from ghost import Ghost
import time
import lxml.html
import urllib2

import log
ghost = Ghost()
url="http://baidu.lecai.com/lottery/draw/view/557/"
session= ghost.start()
session.user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0'
session.wait_timeout=180
session.download_images=False
session.wait_callback=None
session.display=False
session.viewport_size=(800, 600)
session.ignore_ssl_errors=True,
session.plugins_enabled=False
session.java_enabled=False
session.javascript_enabled=True



def BJPK10():
    while True:
        try:
            session.open(url,timeout=180)
        except Exception,err:
            error1= str(err)
            print error1
            log.logging.error('BJKC ERROR:')
            log.logging.exception(error1)
        else:
            html = lxml.html.fromstring(session.content)
            draw_date=html.xpath(u'/html/body/div[6]/div[2]/div[2]/div[2]/div[1]/div[1]/ul/li[1]/h1/b/text()')
            draw_date=''.join(draw_date)
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
            n1=''.join(n1)
            n2=''.join(n2)
            n3=''.join(n3)
            n4=''.join(n4)
            n5=''.join(n5)
            n6=''.join(n6)
            n7=''.join(n7)
            n8=''.join(n8)
            n9=''.join(n9)
            n10=''.join(n10)
            draw_code=n1+','+n2+','+n3+','+n4+','+n5+','+n6+','+n7+','+n8+','+n9+','+n10
            print draw_date,draw_code
            log.logging.info('BJPK10_DrawDate:'+draw_date+' BJPK10_DrawCodes: '+draw_code)
            Open_Web(draw_date,draw_code)
            time.sleep(60)


def Open_Web(drawdate,drawcode):
    callbackurl='http://vir.dogipig.com/lottery/codelist_bjkc.aspx'
    callbackpin='?pin=jinzun110119120'
    callbackurl=callbackurl+callbackpin+'&kjCodes='+drawcode+'&kjExpect='+drawdate
    try:
        response=urllib2.urlopen(callbackurl)
        print response.read()
        log.logging.exception(response.read())
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error('CallBack ERROR:')
        log.logging.exception(error1)
    return


if __name__ == "__main__":
   BJPK10()
