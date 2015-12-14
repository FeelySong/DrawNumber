# coding=utf-8

import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr

import CallAPI
import DrawNO

import multiprocessing

returndate=''

#百度北京pk10
def BJPK10():
    global returndate
    while True:
        #调用爬虫，获取开奖信息
        draw_date,draw_code, draw_time_str= DrawNO.BJPK10()
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=CallAPI.Open_Web(drawdate=draw_date,drawcode=draw_code)
            time.sleep(30)
        time.sleep(10)

def BJPK10_BAIDU_JSON():
    global returndate
    while True:
        #调用爬虫，获取开奖信息
        draw_date,draw_code, draw_time_str= DrawNO.BJPK10_BAIDU_JSON()
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=CallAPI.Open_Web(drawdate=draw_date,drawcode=draw_code)
            time.sleep(30)
        time.sleep(10)

def main():
    # 北京PK10
    jobs=[]
    for i in range(2):
        p_bjkc=multiprocessing.Process(name='bjpk10',target=BJPK10,)
        jobs.append(p_bjkc)
        p_bjkc.start()
        p_bjkc.join(timeout=10)

    jobs=[]
    for i in range(2):
        p_bjpk10_json=multiprocessing.Process(name='bjpk10_json',target=BJPK10_BAIDU_JSON(),)
        jobs.append(p_bjpk10_json)
        p_bjpk10_json.start()
        p_bjpk10_json.join(timeout=10)

if __name__ == "__main__":
    main()