import urllib2
import log
from datetime import datetime

def Open_Web(drawdate,drawcode):
    print 'callapi:'
    print type(drawdate),type(drawcode)
    callbackurl='http://vir.dogipig.com/lottery/codelist_bjkc.aspx'
    callbackpin='?pin=jinzun110119120'
    callbackurl=callbackurl+callbackpin+'&kjCodes='+drawcode+'&kjExpect='+drawdate
    print callbackurl
    try:
        response=urllib2.urlopen(callbackurl)
        calback_result=response.read()
        print calback_result
        log.logging.info('callbackresult:%s time:%s',calback_result,datetime.now().time())
    except Exception,err:
        error1= str(err)
        print error1
        log.logging.error('CallBack ERROR:%s',error1)

    return drawdate