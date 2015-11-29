#!/usr/bin/env python
# -*- coding: cp1252 -*-

from bottle import *
from MySQLdb import *
from MySQLdb.constants import ER


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
    try:
        cnx = connect(user=un, db='people')
    except Error as err:
        reply = False
        if err == ER.DBACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err == ER.BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
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
