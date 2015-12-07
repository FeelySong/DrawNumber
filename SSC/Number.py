# coding=utf-8

import time
import multiprocessing
#from multiprocessing.dummy import Pool as ThreadPool
import sys
import DrawNO
import db
import log
import GDSFC



reload(sys)
sys.setdefaultencoding('utf-8')
sys.excepthook = lambda *args: None
STDERR = sys.stderr

#全局期号
returndate=''

#360重庆时时彩
def ssc360_drawnumber(ssc360_type,db_ssc_type):
    ms_cqssc= db.MSSQL()
    global returndate
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc360_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.CQ360(ssc360_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=ms_cqssc.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
        # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
        # time.sleep(1)
        # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
        time.sleep(30)

# 500wan时时彩
def ssc500_drawnumber(ssc500_type,db_ssc_type):
    ms_cqssc= db.MSSQL()
    global returndate
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc500_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.CP500wan(ssc500_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=ms_cqssc.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
        # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
        # time.sleep(1)
        # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
        time.sleep(30)

#重庆时时彩
def ssc_drawnumber(ssc_type,db_ssc_type):
    ms_cqssc= db.MSSQL()
    global returndate
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.drawnumber(ssc_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=ms_cqssc.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
        # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
        # time.sleep(1)
        # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
        time.sleep(30)

def jxssc_drawnumber(ssc_type,db_ssc_type):
    ms_jxssc= db.MSSQL()
    returnDate=''
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_code, draw_date, draw_time_str= DrawNO.drawnumber(ssc_type)
        if  draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_jxssc.JXCallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)

def gd11x5(ssc_type,db_ssc_type):
    ms_gd11x5= db.MSSQL()
    returndate=''
    while True:
        #调用爬虫，获取开奖信息
        assert isinstance(ssc_type, str)
        draw_date,draw_code, draw_time_str= DrawNO.gd11x5(ssc_type)
        if draw_code == '0' or draw_date <= returndate:
            pass
        else:
            returndate=ms_gd11x5.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)

def tjssc_drawnumber(db_ssc_type):
    ms_tjssc= db.MSSQL()
    returnDate=''
    while True:
        try:
            #调用爬虫，获取开奖信息
            draw_code, draw_date, draw_time_str= DrawNO.tjssc()
            if  draw_code == '0' or draw_date <= returnDate:
                pass
            else:
                returnDate=ms_tjssc.CallSP(lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
                time.sleep(180)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue
#排列三
def pls_drawnumber(db_type):
    ms_pls= db.MSSQL()
    returnDate=''
    while True:
        #调用爬虫，获取开奖信息
        draw_date,draw_code, draw_time_str= DrawNO.PLS()
        if draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_pls.PL3SP(lottery_type=db_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)

#北京PK10
def bjkc_drawnumber(bjkc_db_type):
    ms_bjkc= db.MSSQL()
    bjkcreturndate=''
    while True:
        # #调用爬虫，获取开奖信息
        draw_date,draw_code,draw_time_str= DrawNO.BJKC()
        if  draw_code == '0' or draw_date <= bjkcreturndate:
            pass
        else:
            bjkcreturndate=ms_bjkc.BJKCSP(lottery_type=bjkc_db_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
        time.sleep(180)
    time.sleep(30)

#GDSFC
def gdsf_drawnumber(gdsf_db_type):
    ms_gdsf= db.MSSQL()
    returnDate=''
    while True:
        # #调用爬虫，获取开奖信息
        draw_date,draw_code,draw_time_str= GDSFC.drawnumber()
        if  draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_gdsf.CallSP(lottery_type=gdsf_db_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
        time.sleep(30)


def main():
    """

    :rtype : Null
    """
    #360重庆时时彩
    # ssc360_type='ssccq'
    # db_ssc_type='SSC'
    # jobs=[]
    # for i in range(2):
    #     p_360cq=multiprocessing.Process(name='360CQSSC',target=ssc360_drawnumber,args=(ssc360_type,db_ssc_type,))
    #     jobs.append(p_360cq)
    #     p_360cq.start()
    #     p_360cq.join(timeout=10)

    # #500wan重庆时时彩
    # ssc500_type='ssc'
    # db_ssc_type='SSC'
    # jobs=[]
    # for i in range(2):
    #     p_500cq=multiprocessing.Process(name='500CQSSC',target=ssc500_drawnumber,args=(ssc500_type,db_ssc_type,))
    #     jobs.append(p_500cq)
    #     p_500cq.start()
    #     p_500cq.join(timeout=10)

    # #重庆时时彩
    # ssc_type='cqssc'
    # db_ssc_type='SSC'
    # jobs=[]
    # for i in range(2):
    #     p_cq=multiprocessing.Process(name='CQSSC',target=ssc_drawnumber,args=(ssc_type,db_ssc_type,))
    #     jobs.append(p_cq)
    #     p_cq.start()
    #     p_cq.join(timeout=10)



    # #排列三
    # db_type='PLS'
    # p_cq=multiprocessing.Process(name='PL3',target= pls_drawnumber,args=(db_type,))
    # p_cq.start()
    # p_cq.join(timeout=10)

    # #天津时时彩
    # db_ssc_type='TSC'
    # jobs=[]
    # for i in range(2):
    #     p_tj=multiprocessing.Process(name='TJSSC',target=tjssc_drawnumber,args=(db_ssc_type,))
    #     jobs.append(p_tj)
    #     p_tj.start()
    #     p_tj.join(timeout=10)

    #江西时时彩
    # ssc_type='jxssc'
    # db_ssc_type='XSC'
    # p_jx=multiprocessing.Process(name='JXSSC',target=jxssc_drawnumber,args=(ssc_type,db_ssc_type,))
    # p_jx.start()
    # p_jx.join(10)
    #
    # #广东十分彩
    # gdsf_db_type='GDS'
    # p_gdsf=multiprocessing.Process(name='GDSFC',target=gdsf_drawnumber,args=(gdsf_db_type,))
    # p_gdsf.start()
    # p_gdsf.join(timeout=10)
    #
    # #广东11选5
    # ssc_type='gd11x5'
    # db_11x5_type='SYX'
    # p_11x5=multiprocessing.Process(name='GD11X5',target=gd11x5,args=(ssc_type,db_11x5_type,))
    # p_11x5.start()
    # p_11x5.join(10)

    # 北京PK10
    db_ssc_type='bjkc'
    jobs=[]
    for i in range(2):
        p_bjkc=multiprocessing.Process(name='bjkc',target=bjkc_drawnumber,args=(db_ssc_type,))
        jobs.append(p_bjkc)
        p_bjkc.start()
        p_bjkc.join(timeout=10)

if __name__ == "__main__":
    main()
    # db_ssc_type='TSC'
    # #map_parameters = []
    # #map_parameters.append(db_ssc_type)
    # pool=ThreadPool(2)
    # pool.map(tjssc_drawnumber(db_ssc_type))
    # pool.close()
    # pool.join(timeout=10)