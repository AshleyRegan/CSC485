#!/usr/bin/env python
# -*- coding: cp1252 -*-

from bottle import *
import sqlite3 as lite


@route('/')
def index():
    return '''
            <input type="button" value="Login" onclick="window.location.href='/login'" />
            <img src="http://www.canadianstudebaker.com/Images/canadaflag.gif">
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
    #pw = request.forms.get('pw')
    ans = check(un)
    if ans != 'fail':
        usrpg(ans)
    else:
        return '''
                <p>ERROR: Login failed.</p>
                <br>
                <input type="button" value="Back" onclick="history.back(-1)" />
                <input type="button" value="Home" onclick="window.location.href='/'" />
                '''

@get('/usr')
def check(un):
    conn = lite.connect('people.db')
    c = conn.cursor()
    try:
#    c.executescript("SELECT * FROM Ppl WHERE username='%s' AND password='%s'" % (un, pw))
    	c.executescript("SELECT * FROM Ppl WHERE username = "+ un)
    	reply = c.fetchall()
    except lite.OperationalError:
        reply = 'fail'
    conn.commit()
    c.close()
    return reply

@error(404)
def error404(error):
    return template('''
    		    <input type="button" value="Back" onclick="history.back(-1)" />
                    <input type="button" value="Home" onclick="window.location.href='/'" />
                    <br>
                    ERROR404: Something happened: \n''' + error

@route('/username='+ans[0])
def usrpg(ans):
    return template('''
                    <tr>
			<td>Id</td>
			<td>Username</td>
			<td>Password</td>
			<td>Secret</td>
		    </tr>
		    <tr>
		    	<td>'''+ ans[0] +'''</td>
		    	<td>'''+ ans[1] +'''</td>
		    	<td>'''+ ans[2] +'''</td>
		    	<td>'''+ ans[3] +'''</td>
		    </tr>
                    <br>
                    <input type="button" value="Back" onclick="history.back(-1)" />
                    <input type="button" value="Home" onclick="window.location.href='/'" />
                    ''')
    
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)
