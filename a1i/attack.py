#!/usr/bin/env python

from webtest import TestApp
import test

def injectionattack():
    app = TestApp(test.app)
    app.post('/login', {'username':'user','password':'pass'})
    assert app.get('/admin').status == '200 OK'
    app.get('/logout')
    app.reset()
    assert app.get('/admin').status == '401 Unauthorized'
    
 

# '; DROP TABLE Ppl; --'
# '; SELECT * FROM Ppl INTO OUTFILE "/attack.txt"'

if __name__ == '__main__':
    
