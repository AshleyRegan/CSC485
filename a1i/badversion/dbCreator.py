#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

#creates database
con = lite.connect('people.db')

with con:
    #creates a cursor to work with database
    cur = con.cursor()   
    #creates table & labels column ids
    cur.execute("CREATE TABLE Ppl(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, secret CHAR(100))")
    #populating the table
    cur.execute('''INSERT INTO Ppl VALUES("admin", "123", "I don't know what I'm doing")''')
    cur.execute('''INSERT INTO Ppl VALUES("user", "pass", "I have no imagination")''')
    cur.execute('''INSERT INTO Ppl VALUES("can", "sux", "This is not a secret")''')
    cur.execute('''INSERT INTO Ppl VALUES("johnny", "you", "You're not actually johnny")''')

con.commit()
cur.close()
