# coding=utf-8
__author__ = 'Feely'

import time
import multiprocessing
import sys
import PLSDrawNO
import dbpls

reload(sys)
sys.setdefaultencoding('utf-8')
sys.excepthook = lambda *args: None
STDERR = sys.stderr
sys.path.append('/data/app/PROJZDrawNumber/PLS')

#排列三
def pls_drawnumber(db_type):
    ms_pls= dbpls.MSSQL()
    returnDate=''
    while True:
        draw_date,draw_code, draw_time_str= PLSDrawNO.PLS()
        if draw_code == '0' or draw_date <= returnDate:
            pass
        else:
            returnDate=ms_pls.PL3SP(lottery_type=db_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time_str)
            time.sleep(180)
        time.sleep(30)


def main():
    db_type='PLS'
    p_cq=multiprocessing.Process(name='PL3',target= pls_drawnumber,args=(db_type,))
    p_cq.start()
    p_cq.join(timeout=10)


if __name__ == "__main__":
    main()