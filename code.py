#!/usr/bin/python

import sqlite3 as lite
import sys

import web

render = web.template.render('templates/')

urls = (
   '/', 'index',
   '/hello', 'hellworld'
)

class helloworld:
   def GET(self):
        return "Hello, world!"

class add:
    def POST(self):
        i = web.input()
        n = db.insert('ppl', username=i.un, password=i.pw)
        raise web.seeother('/')

class index:
   def GET(self):
        i = web.input(name=None)
        return render.index(i.name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
