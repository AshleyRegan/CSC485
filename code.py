import web

render = web.template.render('templates/')

urls = (
   '/', 'index',
   '/hello', 'hellworld'
)

class helloworld:
   def GET(self):
        return "Hello, world!"


class index:
   def GET(self):
        i = web.input(name=None)
        return render.index(i.name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
