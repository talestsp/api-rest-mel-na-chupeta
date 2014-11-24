#!/usr/bin/env python
# -*- coding: utf-8 -*-


import csv
import json 
import sqlite3 as lite
import sys

def create_connection():
    db_name = "subset_artist_term"
    con = lite.connect('database/subset_artist_term.db')
    return con

def state_location_by_artist_id(artist_id):
    try:
        cnxn = create_connection()
        cursor = cnxn.cursor()
        query = "SELECT * FROM artist_mbtag;"
        #query = "SELECT id, state FROM usa_artist_state_locatio WHERE id =" + id + ";"
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

def artist_id_by_state_location(state):
    try:
        cnxn = create_connection()
        cursor = cnxn.cursor()
        query = "SELECT * FROM artist_mbtag;"
        #query = "SELECT id, state FROM usa_artist_gps_location WHERE state =" + state + ";"
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

def montaJson(spamreader, col):
        response = []
        colunas = col
        i = 0
        for row in spamreader:
                celulas = {}
                for indexColumns in range(0,len(colunas)):
                        celulas[colunas[indexColumns]] = row[indexColumns]
                response.append(celulas)
                i = i + 1;
        return response