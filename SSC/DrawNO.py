# coding=utf-8

import socket
import time
from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup
import urllib2
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr
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

def drawnumber(ssc_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
    except Exception,err:
        error1= str(err)
        print ssc_type,error1
        log.logging.error(br.title())
        log.logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        draw_date = result[18:30]
        draw_code = result[46:51]
        draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[65:81].strip()
        print draw_date, draw_code1, draw_time,datetime.now()
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code1,draw_time,datetime.now().time())
        #print result
        return draw_date,draw_code1,draw_time

def tjssc():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://www.tjflcpw.com'
    now_time=time.localtime()
    number = ''
    try:
        r = br.open(url,timeout=10)
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error(br.title())
        log.logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        draw_date = d.xpath(u'/html/body/form/div[4]/div[3]/div[2]/div/div[5]/div[1]/span[2]/a/text()')[0].decode('utf-8')
        print draw_date
        draw_date = draw_date[42:50]+'-'+draw_date[50:53]
        number = number+''.join(d.xpath(u'/html/body/form/div[4]/div[3]/div[2]/div/div[5]/div[2]/ul/li[1]/text()'))+','
        number = number+''.join(d.xpath(u'/html/body/form/div[4]/div[3]/div[2]/div/div[5]/div[2]/ul/li[2]/text()'))+','
        number = number+''.join(d.xpath(u'/html/body/form/div[4]/div[3]/div[2]/div/div[5]/div[2]/ul/li[3]/text()'))+','
        number = number+''.join(d.xpath(u'/html/body/form/div[4]/div[3]/div[2]/div/div[5]/div[2]/ul/li[4]/text()'))+','
        number = number+''.join(d.xpath(u'/html/body/form/div[4]/div[3]/div[2]/div/div[5]/div[2]/ul/li[5]/text()'))
        draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
        print draw_date,number,draw_time
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,number,draw_time,datetime.now().time())
        #print result
        return number,draw_date,draw_time

def tjsscbak():
    url="http://kj.cjcp.com.cn/tjssc/"
    r = br.open(url,timeout=10)
    html = r.read()
    print br.title()
    soup = BeautifulSoup(html)
    table_hot = soup.find('td',attrs={"class":"qihao"})
    time_hot = soup.find ('td',attrs={"class":"time"})
    draw_time=time_hot.get_text()
    date_tmp=table_hot.get_text()
    draw_date=date_tmp[0:8]+'-0'+date_tmp[9:11]
    number1 = {}
    codes=''
    t1=0
    # print soup.find('td', text=table_hot.get_text()).parent.find_all('input')['value']
    while t1<5:
        number1[t1]=soup.find("td", text=table_hot.get_text()).parent.find_all('input')[t1]['value']
        codes=codes+number1[t1].strip()+','
        t1+=1
    draw_code=codes[:-1]
    print "tjssc number:"
    print draw_code,draw_date,draw_time
    log.logging.info('天津时时彩'+'   '+url)
    log.logging.info('date:%s code:%s curtime:%s',draw_date,draw_code,datetime.now())
    return draw_code,draw_date,draw_time[:-3]

def gd11x5(ssc_type):
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
    except Exception,err:
        error=str(err)
        print error
        log.logging.error(br.title())
        log.logging.error(error)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        #Show the response headers
        #print r.info()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        draw_date = result[15:27]
        draw_code = result[43:57]
        #draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[71:87].strip()
        print draw_date, draw_code, draw_time,datetime.now()
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s',draw_date,draw_code,draw_time)
        #print result
        return draw_date,draw_code,draw_time

def PLS():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://caipiao.163.com/order/pl3/'
    try:
        r = br.open(url)
    except Exception,err:
        error1= str(err)
        print 'pls',error1
        log.logging.error(br.title())
        log.logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        draw_date_tmp = d.xpath(u'//b[@class="c_ba2636"]/text()')[10].encode("utf-8")
        #print draw_date_tmp
        draw_date=draw_date_tmp[5:10]
        #print draw_date
        draw_code_tmp = d.xpath(u'//b[@class="c_ba2636"]/text()')[11].encode("utf-8")
        #print draw_code_tmp
        draw_code=draw_code_tmp[0]+','+draw_code_tmp[2]+','+draw_code_tmp[4]
        #print draw_code
        draw_time_tmp = d.xpath(u'//div[@class="n_kjgg"]/text()')[2].encode("utf-8")
        draw_time=draw_time_tmp[20:40]
        #print draw_time
        print draw_date, draw_code, draw_time,datetime.now()
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
        return draw_date,draw_code,draw_time

def CQ360(ssc360_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://cp.360.cn/'+ssc360_type+'/'
    now_time=time.localtime()
    number = ''
    try:
        r = br.open(url,timeout=10)
    except Exception,err:
        error= str(err)
        print 'CQ360',error
        log.logging.error(br.title())
        log.logging.exception(error)
        return '0','0','0'
    else:
        ssc_html = r.read()
        #print ssc_html
        #show the html title
        print '360时时彩',url
        #print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        #Draw DateNO
        draw_date_tmp = ''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/h3/em/text()'))
        #draw_date_tmp = ''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/h3/em/text()'))
        draw_date=str(now_time.tm_year)+draw_date_tmp[0:4]+'-'+draw_date_tmp[4:7]
        #drow Number
        number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]/text()'))+','
        number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[2]/text()'))+','
        number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]/text()'))+','
        number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[4]/text()'))+','
        number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[5]/text()'))
        draw_code=number
        #Draw Time
        draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
        print draw_date,draw_code,datetime.now()
        if (number=='?,?,?,?,?'):
            number='0'
        log.logging.info('360时时彩'+'   '+url)
        log.logging.info('date:%s code:%s curtime:%s',draw_date,draw_code,datetime.now())
        return draw_date,number,draw_time

def CP500wan(ssc500_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """

    url="http://www.500wan.com/static/public/"+ssc500_type+"/xml/newlyopen.xml"
    print url
    now_time=time.localtime()
    number = ''
    try:
        r = br.open(url,timeout=10)
    except Exception,err:
        error= str(err)
        print 'CQ360',error
        log.logging.error(br.title())
        log.logging.exception(error)
        return '0','0','0'
    else:
        html = r.read()
        print html
        draw_date=html[58:66]+'-'+html[66:69]
        draw_code=html[81:90]
        draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
        print draw_date,draw_code,draw_time
        if (draw_code=='?,?,?,?,?'):
            draw_code='0'
        log.logging.info('500wan时时彩'+'   '+url)
        log.logging.info('date:%s code:%s curtime:%s',draw_date,draw_code,datetime.now())
        return draw_date,draw_code,draw_time

def CQBaidu():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://www.lecai.com/lottery/cqssc/'
    try:
        r = br.open(url)
    except Exception,err:
        error1= str(err)
        print 'pls',error1
        log.logging.error(br.title())
        log.logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        print ssc_html

        #show the html title
        print br.title()
        # xpath analyze
        d = etree.HTML(ssc_html)
        draw_date_tmp = d.xpath(u'/html/body/div[7]/div[2]/div[2]/div[2]/table[1]/tbody/tr[2]/td[1]/text()')
        print draw_date_tmp

def BJKC():
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://www.bwlc.gov.cn/bulletin/prevtrax.html'
    try:
        r = br.open(url,timeout=30)
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error(br.title())
        log.logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        mathnum=ssc_html.find('期号')
        tmpstring=ssc_html[mathnum+500:mathnum+600]
        print  tmpstring
        draw_date=tmpstring[1:7]
        draw_code=tmpstring[25:54]
        draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
        print draw_date,draw_code,draw_time
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
        #print result
        return draw_date,draw_code,draw_time

def CQSSC_BAIDU_JSON(lottery_type):
    url='http://www.lecai.com/lottery/ajax_latestdrawn.php?lottery_type='+lottery_type
    print url
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
        draw_date=draw_date[0:8]+'-'+draw_date[8:11]
        # dics=subvalue[0]
        number=subvalue[0]['result']['result'][0]['data']
        draw_code=number[0]+','+number[1]+','+number[2]+','+number[3]+','+number[4]
        draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
        print 'BJPK10_BAIDU_JSON:'
        print draw_date,draw_code,draw_time
        log.logging.info('Source Title:CQSSC_JSON')
        log.logging.info('date:%s code:%s time:%s',draw_date,draw_code,draw_time)
        if draw_code == ',,,,,,,,,':
            draw_code='0'
        return draw_date,draw_code,draw_time
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error('CQSSC_JSON ERROR:%s',error1)
        return '0','0','0'


