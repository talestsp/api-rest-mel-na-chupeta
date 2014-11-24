#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import json 
import sqlite3 as lite
import sys

def create_connection(db_name):
    con = lite.connect('../database/' + db_name '.db')
    return con

def state_location_by_artist_id(artist_id):
    try:
        cnxn = create_connection()
        cursor = cnxn.cursor()
        query = "SELECT id, state FROM usa_artist_state_location WHERE id =" + id + ";"
        print query
        cursor.execute(query)
        rows = cursor.fetchall()
        cnxn.close()
        lista_tuplas = []
        for tupla in rows:
           lista_tuplas.append(tupla)
        col = ["artist_id", "state"]
        response = montaJson(lista_tuplas, col)
        return json.dumps(response).encode("utf-8")

def artist_id_by_state_location(state):
    try:
        cnxn = create_connection()
        cursor = cnxn.cursor()
        query = "SELECT id, state FROM usa_artist_state_location WHERE state =" + state + ";"
        print query
        cursor.execute(query)
        rows = cursor.fetchall()
        cnxn.close()
        lista_tuplas = []
        for tupla in rows:
           lista_tuplas.append(tupla)
        col = ["artist_id", "state"]
        response = montaJson(lista_tuplas, col)
        return json.dumps(response).encode("utf-8")
    
    except lite.Error, e:
        return "Error %s:" % e.args[0]

    finally:
        if con:
            con.close()