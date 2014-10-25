__author__ = 'Feely'
import web
import model

### Url mappings

urls = (
    '/', 'Index',
    '/Getdata/(.*?)', 'Getdata'
)

### Templates
render = web.template.render('templates',base='base')

class Index:
    def GET(self):
        return render.index()

class Getdata:
    def POST(self,id):
        iddata=web.data()
        print iddata
        todor=model.get_todos(id)
        return render.Getdata(todor)

# class Update:
#
#     def POST(self, username,qihao,DrawNO):
#         """ Delete based on ID """
#         model.update(username,qihao,DrawNO)
#         raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
