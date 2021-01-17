import os
from flask import Flask, request, jsonify
from geocode_module import reverse_geocode
from db_module import district_db, location_db
from clustering_algo import clustering

ddb = district_db()
ldb = location_db()

app =  Flask(__name__)

@app.route('/api/postData', methods=['POST'])
def write_to_db():
    data = request.get_json()
    coordinates = data['coordinates']
    address = reverse_geocode(coordinates)
    postcode = address.split(',')[-1].strip()

    coordinates = clustering(postcode, coordinates)
    params = {'coordinates': coordinates, 'address': address, 'image': data['image'], 'last_seen': data['timestamp'], 'amount': data['amount'], 'status': data['status']}
    ddb.add_location(postcode, params)
    location_id = ddb.get_location_id(postcode, coordinates)
    ldb.add_sighting(location_id, {'time': data['timestamp'], 'amount': data['amount']})

    return 'OK', 200

@app.route('/api/getData', methods=['GET'])
def read_from_db():
    args = request.args
    coordinates = args['query']

    address = reverse_geocode(coordinates)
    postcode = address.split(',')[-1].strip()
    location_id = ddb.get_location_id(postcode, coordinates)

    return jsonify(ldb.get_location_data(location_id))

if __name__ == '__main__':
    app.run(host='localhost', port='4000', debug=False)
