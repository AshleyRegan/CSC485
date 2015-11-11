#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

#creates database
con = lite.connect('people.db')

with con:
    cur = con.cursor()   
    #creates table & labels column ids
    cur.execute("CREATE TABLE Ppl('#' INT, Name TEXT, 'Last name' TEXT, 'Birth date' TEXT, Role TEXT, Department TEXT, 'E-mail' TEXT)")
    #populating the table
    cur.execute("INSERT INTO Ppl VALUES(101,'John','Smith','12-12-1980','Manager','Sales','john.smith@abc.com')")
    cur.execute("INSERT INTO Ppl VALUES(102,'Laura','Adams','02-11-1979','Manager','IT','laura.adams@abc.com')")
    cur.execute("INSERT INTO Ppl VALUES(103,'Peter','Williams','22-10-1966','Coordinator','HR','peter.williams@abc.com')")
    cur.execute("INSERT INTO Ppl VALUES(104,'Joana','Sanders','11-11-1976','Manager','Marketing','joana.sanders@abc.com')")
    cur.execute("INSERT INTO Ppl VALUES(105,'John','Drake','18-08-1988','Coordinator','Finance','john.drake@abc.com')")
    cur.execute("INSERT INTO Ppl VALUES(106,'Samuel','Williams','22-03-1985','Coordinator','Finance','samuel.williams@abc.com)")
