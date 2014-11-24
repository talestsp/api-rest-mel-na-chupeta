#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json 
import sqlite3 as lite
import sys

def create_connection(db_name):
    db_name = "subset_artist_term"
    con = lite.connect('database/' + db_name + '.db')
    return con

#busca o estado relacionado a banda
def state_location_by_artist_id(artist_id):
    try:
        cnxn = create_connection()
        cursor = cnxn.cursor()

        #uma simples consulta para ver se o db funciona
        query = "SELECT * FROM artist_mbtag;"
        
        #esta é a consulta que deve ser realizada quando o bd estiver funcionando
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

#busca as bandas relacionadas ao estado
def artist_id_by_state_location(state):
    try:
        cnxn = create_connection()
        cursor = cnxn.cursor()
        
        #uma simples consulta para ver se o db funciona
        query = "SELECT * FROM artist_mbtag WHERE artist_id ='AR00A6H1187FB5402A';"
        
        #esta é a consulta que deve ser realizada quando o bd estiver funcionando
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

#enquanto o bd nao funciona, csv :)
def artist_id_by_state_location_csv(state):
    try:
        arq = open("database/csv/usa_artist_state_location.csv")
        query_json = []

        #dispensa o cabeçalho
        arq.readline()
        
        lines = arq.readlines()
        for line in lines:
            split_line = line.split(",")
            print split_line[3].lower().replace("\n",""), ",", state.lower().replace("\n","")
            if (split_line[3].lower().replace("\n","") == state.lower().replace("\n","")):
                tupl = {}
                tupl["artist_id"] = split_line[0].replace("\n","")
                tupl["state"] = split_line[3].lower().replace("\n","")
                query_json.append(tupl)

        print ">>> "
        print query_json
        return json.dumps(query_json)

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