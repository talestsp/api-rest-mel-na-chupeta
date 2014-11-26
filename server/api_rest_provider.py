#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, make_response, request
import api_rest_data
import os

app = Flask(__name__)

@app.route('/tags_by_state', methods=['GET'])
def tags_by_states():
    state = request.args['state']
    response = api_rest_data.tags_by_state(state)
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@app.route('/states_by_tag', methods=['GET'])
def states_by_tag():
    state = request.args['state']
    response = api_rest_data.states_by_tag(state)
    response = make_response(response)
    response.headers['Access

@app.route('/artist_id_by_state_location', methods=['GET'])
def artist_id_by_state_location_csv():
    state = request.args['state']
    response = api_rest_data.artist_id_by_state_location_csv(state)
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@app.route('/tags_states')
def tags_states():
    response = api_rest_data.tags_states()
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

if __name__ == '__main__':
    
    app.debug = True    
    app.run(host='0.0.0.0', port=9090)