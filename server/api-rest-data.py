#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('database/db.h2.db')
    
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data

    print "----"
    tableListQuery = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
    cur.execute(tableListQuery)
    tables = map(lambda t: t[0], cur.fetchall())
    print "----"

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()