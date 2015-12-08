# coding=utf-8


import time
import lxml.html
import urllib2
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr

import log
import multiprocessing


def BJKC():
    import socket
    from datetime import datetime

    import mechanize
    import cookielib
    import log

    socket.setdefaulttimeout(30)

    #Browser
    br = mechanize.Browser()
    cj = cookielib.CookieJar()
    br.set_cookiejar(cj)
    #Browser options
    br.set_handle_equiv(True)
    ##br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    #Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize.HTTPRefreshProcessor(), max_time=1)
    #User-Agent
    br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0")]

    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://www.bwlc.gov.cn/bulletin/prevtrax.html'
    while True:
        try:
            r = br.open(url,timeout=30)
        except Exception,err:
            error1= str(err)
            print error1
            log.logging.error(br.title().encode('gbk'))
            log.logging.exception(error1)
            return '0','0','0'
        else:
            ssc_html = r.read().decode('utf-8')
            #show the html title
            print br.title().encode('gbk')
            mathnum=ssc_html.find('期号')
            tmpstring=ssc_html[mathnum+500:mathnum+600]
            # print  tmpstring
            draw_date=tmpstring[1:7]
            draw_code=tmpstring[25:54]
            draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
            print draw_date,draw_code,draw_time
            log.logging.info(br.title().encode('gbk'))
            log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
            Open_Web(draw_date,draw_code)

            #print result
            # return draw_date,draw_code,draw_time
        time.sleep(30)
    return

def BJPK10_BaiDu():

    from ghost import Ghost
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

    while True:
        try:
            session.open(url,timeout=180)
            # page, resources=session.wait_for_page_loaded()
        except Exception,err:
            error1= str(err)
            print error1
            log.logging.error('BJKC ERROR:%s',error1)
        else:
            html = lxml.html.fromstring(session.content)
            Source_Title=html.xpath(u'/html/head/title/text()')
            print Source_Title[0].encode('gbk')
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
            log.logging.info('Source Title:%s',Source_Title[0].encode('gbk'))
            log.logging.info('date:%s code:%s time:%s',draw_date,draw_code,datetime.now().time())
            if draw_code != ',,,,,,,,,':
                Open_Web(draw_date,draw_code)
        time.sleep(30)
    return

def Open_Web(drawdate,drawcode):
    callbackurl='http://vir.dogipig.com/lottery/codelist_bjkc.aspx'
    callbackpin='?pin=jinzun110119120'
    callbackurl=callbackurl+callbackpin+'&kjCodes='+drawcode+'&kjExpect='+drawdate
    try:
        response=urllib2.urlopen(callbackurl)
        print response.read()
        log.logging.info('callbackresult:%s time:%s',str(response.read()),datetime.now().time())
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error('CallBack ERROR:%s',error1)
    return


if __name__ == "__main__":
    # 北京PK10
    jobs=[]
    for i in range(2):
        p_bjkc_baidu=multiprocessing.Process(name='bjkc',target=BJKC,)
        jobs.append(p_bjkc_baidu)
        p_bjkc_baidu.start()
        p_bjkc_baidu.join(timeout=10)

    time.sleep(30)

    #百度北京PK10
    jobs=[]
    for i in range(2):
        p_bjkc=multiprocessing.Process(name='bjkc',target=BJPK10_BaiDu,)
        jobs.append(p_bjkc)
        p_bjkc.start()
        p_bjkc.join(timeout=10)
        time.sleep(10)

