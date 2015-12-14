# coding=utf-8

import urllib2
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr

import socket
import time
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

def BJPK10():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://www.bwlc.gov.cn/bulletin/prevtrax.html'
    try:
        r = br.open(url,timeout=30)
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
        if draw_code==',,,,,,,,,':
            draw_code='0'
        return draw_date,draw_code,draw_time
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error(br.title().encode('gbk'))
        log.logging.exception(error1)
        return '0','0','0'

def BJPK10_BAIDU_JSON():
    url='http://www.lecai.com/lottery/ajax_latestdrawn.php?lottery_type=557'
    try:
        response=urllib2.urlopen(url)
        datas=response.read()
        value=json.loads(datas)
        rootlist = value.keys()
        # print rootlist
        # for rootkey in rootlist:
        #     print rootkey
        subvalue = value['data']
        draw_date=subvalue[0]['phase']
        # dics=subvalue[0]
        number=subvalue[0]['result']['result'][0]['data']
        draw_code=number[0]+','+number[1]+','+number[2]+','+number[3]+','+number[4]+','+number[5]+','+number[6]+','+number[7]+','+number[8]+','+number[9]
        draw_time=datetime.now().time()
        print 'BJPK10_BAIDU_JSON:'
        print draw_date,draw_code
        log.logging.info('Source Title:BJCK_JSON')
        log.logging.info('date:%s code:%s time:%s',draw_date,draw_code,draw_time)
        if draw_code == ',,,,,,,,,':
            draw_code='0'
        return draw_date,draw_code,draw_time
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error('BJKC_JSON ERROR:%s',error1)
        return '0','0','0'