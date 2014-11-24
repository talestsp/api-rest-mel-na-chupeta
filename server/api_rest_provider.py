#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, make_response, request
import api_rest_data

app = Flask(__name__)

@app.route('/state_location_by_artist_id', methods=['GET'])
def state_location_by_artist_id():
        id = request.args['id']
        response = api_rest_data.state_location_by_artist_id(id)
        response = make_response(response)
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response

@app.route('/artist_id_by_state_location', methods=['GET'])
def artist_id_by_state_location():
        state = request.args['state']
        response = api_rest_data.artist_id_by_state_location(state)
        response = make_response(response)
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response

if __name__ == '__main__':
    app.debug = True    
    app.run(host='0.0.0.0', port=9090)