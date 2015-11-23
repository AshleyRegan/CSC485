#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

#creates database
con = lite.connect('people.db')

with con:
    cur = con.cursor()   
    #creates table & labels column ids
    cur.execute("CREATE TABLE Ppl(username TEXT, password TEXT)")
    #populating the table
    cur.execute('''INSERT INTO Ppl VALUES("johnny", "you")''')
