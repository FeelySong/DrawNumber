__author__ = 'Feely'
import web

db = web.database(dbn='mssql', host='223.252.163.80', port='60000', db='ibc', user='jzviradmin', pw='1qaz2wsx')

def get_todos(id):
    sql="select cardno from tbBindBankCard where id="+str(id)
    print sql
    results=db.query(sql)
    for result in results:
        print result.cardno
    return result.cardno


# def new_todo(text):
#     db.insert('todo', title=text)
#
# def del_todo(id):
#     db.delete('todo', where="id=$id", vars=locals())

