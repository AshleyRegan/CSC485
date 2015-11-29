#!/usr/bin/env python
# -*- coding: cp1252 -*-

from bottle import *
import sqlite3 as lite


@route('/')
def index():
    return '''
            <input type="button" value="Login" onclick="window.location.href='/login'" />
            <input type="button" value="Sign Up" onclick="window.location.href='/signup'" />
            '''

@route('/login')
def loginpg():
    return template('''
        <form action="/login" method="post">
            Username: <input placeholder="Username" name="un" type="text" />
            Password: <input placeholder="Password" name="pw" type="password" />
            <input value="Login" type="submit" />
        </form>
        ''')

@post('/login')
def login():
    un = request.forms.get('un')
    pw = request.forms.get('pw')
    if check(un, pw):
        redirect('/username='+un+'+password='+pw)
    else:
        return '''
                <p>ERROR: Login failed.</p>
                <br>
                <input type="button" value="Back" onclick="history.back(-1)" />
                <input type="button" value="Home" onclick="window.location.href='/'" />
                '''

@get('/usr')
def check(un, pw):
    reply = True
    conn = lite.connect('people.db')
    c = conn.cursor()
##    try:
    c.executescript("SELECT * FROM Ppl WHERE username='%s' AND password='%s'" % (un, pw))
    result = c.fetchall()
##    except lite.OperationalError:
##        reply = False
    conn.commit()
    c.close()
    return reply

@error(404)
def error404(error):
    return 'ERROR404: Wow! Where did the db go??'

@route('/username=<un>+password=<pw>')
def usrpg(un, pw):
    return template('''
                    <p>Welcome {{name}}! Enjoy your {{pas}}!
                    <br>
                    <input type="button" value="Back" onclick="history.back(-1)" />
                    <input type="button" value="Home" onclick="window.location.href='/'" />
                    ''', name=un, pas=pw)
    
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
