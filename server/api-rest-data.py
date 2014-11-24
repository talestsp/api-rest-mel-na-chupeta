#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    #este eh o do problema2, funciona
    con = lite.connect('/home/tales/development/Git/ad2/ad2-p2/data/AdditionalFiles/subset_artist_term.db')
    cur = con.cursor()

    #lista as tabelas
    tableListQuery = "select name from sqlite_master where type = 'table'"
    print "TABELAS"
    cur.execute(tableListQuery)
    data = cur.fetchall()
    print data
    
    print

    #este eh o do problema3, nao funciona, esta ecrypted
    con = lite.connect('/home/tales/development/Git/api-rest-mel-na-chupeta/database/db.trace.db')
    cur = con.cursor()

    #lista as tabelas
    tableListQuery = "select name from sqlite_master where type = 'table'"
    print "TABELAS"
    cur.execute(tableListQuery)
    data = cur.fetchall()
    print data
   

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()