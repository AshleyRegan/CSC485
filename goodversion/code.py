#!/usr/bin/python

import sqlite3 as lite
import sys

import web

render = web.template.render('templates/')

urls = (
   '/', 'index',
   '/hello', 'hellworld',
   '/add', 'add'
)

class helloworld:
   def GET(self):
        return "Hello, world!"

class add:
    def POST(self):
       conn = lite.connect('people.db')
       c = conn.cursor()
       i = web.input()
       c.execute("INSERT INTO Ppl(username, password) VALUES('" + i.un + "', '" + i.pw + "')")
       conn.commit()
       
class index:
   def GET(self):
        i = web.input(name=None)
        return render.index(i.name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

