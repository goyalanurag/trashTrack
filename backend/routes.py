import os
from flask import Flask, request, jsonify
from modules.geocode_module import reverse_geocode
from modules.db_module import district_db, location_db
from modules.clustering_algo import clustering
from ml_model.trash_detection import scan_and_call
from time import sleep
from multiprocessing import Process

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

def process_1():
    app.run(host='localhost', port='4000', debug=False)

def process_2():
    while True:
        scan_and_call()
        sleep(120)

if __name__ == '__main__':
    p1 = Process(target=process_1)
    p2 = Process(target=process_2)
    p1.start(); p2.start()
    p1.join(); p2.join()
