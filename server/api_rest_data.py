#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json 
import sqlite3 as lite
import sys
import os
from collections import Counter

def create_connection(db_name):
    #retirar a linha a seguir
    db_name = "subset_artist_term"
    con = lite.connect('database/' + db_name + '.db')
    return con

#enquanto o bd nao funciona, csv :)
def tags_by_state(state):
        path = os.path.dirname(os.path.realpath(__file__)).split("/")
        path = "/".join(path[:-1])
        
        state_siglas_arq = open("../database/state_siglas.csv")
        artist_mbtag_arq = open("../database/artist_mbtag.csv")
        
        ocorrencias = []

        #dispensa o cabeçalho
        state_siglas_arq.readline()
        artist_mbtag_arq.readline()
        
        state_lines = state_siglas_arq.readlines()
        artist_lines = artist_mbtag_arq.readlines()

        artista_do_state = []

        for linha in state_lines:
            if(linha.split(",")[1].replace("\n", "") == state.replace("'","")):
                artista_do_state.append(linha.split(",")[0])
        
        for linha in artist_lines:
            if(linha.split(",")[0] in artista_do_state):
                ocorrencias.append(linha.split(",")[1].replace("\n", ""))
                print linha.split(",")[1].replace("\n", "")

        query_json = []

        

        for i in ocorrencias.keys():

        
        return json.dumps(Counter(ocorrencias))

#enquanto o bd nao funciona, csv :)
def artist_id_by_state_location_csv(state):
    try:
        arq = open("../database/csv/usa_artist_state_location.csv")
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

#enquanto o bd nao funciona, csv :)
def tags_states():
    try:
        print ">>> ", os.getcwd()
        arq = open("/home/tales/development/Git/api-rest-mel-na-chupeta/database/csv/usa_artist_state_location.csv")
        state_tags = []
        

        #dispensa o cabeçalho
        arq.readline()
        
        lines = arq.readlines()
        for line in lines:
            split_line = line.split(",")
            state = split_line[3]

            print split_line[3].lower().replace("\n",""), ",", state.lower().replace("\n","")
            
            if (split_line[3].lower().replace("\n","") == state.lower().replace("\n","")):
                tupl = {}
                tupl["artist_id"] = split_line[0].replace("\n","")
                tupl["state"] = split_line[3].lower().replace("\n","")
                state_tags.append(tupl)

        print ">>> "
        print state_tags
        return json.dumps(state_tags)

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

#busca o estado relacionado a banda
def state_location_by_artist_id(artist_id):
    try:
        cnxn = create_connection("NOME_DO_BD")
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
