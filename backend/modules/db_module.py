import mysql.connector

class district_db:

    def __init__(self):
        self.db = mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='CR237ZAG20',
                                          database='districts')
        self.cursor = self.db.cursor()

    def district_exists(self, postcode):
        self.db.commit()
        self.cursor.execute('SHOW TABLES;')
        tables = [table[0] for table in self.cursor]
        if postcode in tables:
            return True
        return False

    def add_district(self, postcode):
        if not self.district_exists(postcode):
            self.db.commit()
            query = f'CREATE TABLE {postcode} (id INT NOT NULL AUTO_INCREMENT, coordinates VARCHAR(20) NOT NULL, address VARCHAR(255) NOT NULL, image VARCHAR(255) NOT NULL, sightings INT NOT NULL, last_seen TIMESTAMP NOT NULL, amount VARCHAR(255) NOT NULL, status VARCHAR(255) NOT NULL, PRIMARY KEY(id));'
            self.cursor.execute(query)
            self.db.commit()

    def location_exists(self, postcode, coordinates):
        self.db.commit()
        coordinates = coordinates.replace(' ', '')
        self.cursor.execute(f'SELECT id FROM {postcode} WHERE coordinates = \'{coordinates}\';')
        locations = [location[0] for location in self.cursor]
        if len(locations) > 0:
            return True
        return False

    def get_location_id(self, postcode, coordinates):
        coordinates = coordinates.replace(' ', '')
        if self.location_exists(postcode, coordinates):
            self.db.commit()
            query = f'SELECT id FROM {postcode} WHERE coordinates = \'{coordinates}\';'
            self.cursor.execute(query)
            id = [n for n in self.cursor][0][0]
            return id
        return None

    def add_location(self, postcode, data):
        data['coordinates'] = data['coordinates'].replace(' ', '')
        self.add_district(postcode)
        if self.location_exists(postcode, data['coordinates']):
            query = f"SELECT sightings FROM {postcode} WHERE coordinates = \'{data['coordinates']}\';"
            self.cursor.execute(query)
            new_sightings = [n[0] for n in self.cursor][0] + 1
            query = f"UPDATE {postcode} SET sightings = {new_sightings} WHERE coordinates = \'{data['coordinates']}\';"
            self.cursor.execute(query)
            self.db.commit()
        else:
            self.db.commit()
            query = f'INSERT INTO {postcode} (coordinates, address, image, sightings, last_seen, amount, status)'
            query += f" VALUES (\'{data['coordinates']}\', \'{data['address']}\', \'{data['image']}\', 1, \'{data['last_seen']}\', \'{data['amount']}\', \'{data['status']}\');"
            self.cursor.execute(query)
            self.db.commit()
            ldb = location_db()
            ldb.add_location(self.get_location_id(postcode, data['coordinates']))
            self.db.commit()

    def get_all_coordinates(self, postcode):
        self.db.commit()
        self.cursor.execute(f'SELECT coordinates FROM {postcode};')
        coordinates = [cdt[0] for cdt in self.cursor]
        return coordinates

    def get_all_locations(self, postcode):
        self.db.commit()
        query = f'SELECT * FROM {postcode} WHERE id = \'{id}\''
        self.cursor.execute(query)
        result = {'locations': []}
        for row in self.cursor:
            location = {'id': row[0], 'coordinates': row[1], 'address': row[2], 'image': row[3], 'sightings': row[4], 'last_seen': row[5], 'amount': row[6], 'status': row[7]}
            result['locations'].append(location)
        return result


class location_db:

    def __init__(self):
        self.db = mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='CR237ZAG20',
                                          database='locations')
        self.cursor = self.db.cursor()

    def location_exists(self, location_id):
        self.db.commit()
        self.cursor.execute('SHOW TABLES;')
        tables = [table[0] for table in self.cursor]
        if location_id in tables:
            return True
        return False

    def add_location(self, location_id):
        if not self.location_exists(location_id):
            self.db.commit()
            query = f'CREATE TABLE location{location_id} (id INT NOT NULL AUTO_INCREMENT, time TIMESTAMP NOT NULL, amount VARCHAR(255), increment INT(11), PRIMARY KEY (id));'
            self.cursor.execute(query)
            self.db.commit()

    def add_sighting(self, location_id, data):
        self.db.commit()
        increment = 1
        query = f'SELECT amount FROM location{location_id} ORDER BY id DESC;'
        self.cursor.execute(query)
        amount = [n for n in self.cursor]
        if len(amount) > 0:
            amount = amount[0][0]
            amount_map = {'low': 1, 'medium': 2, 'high': 3}
            if amount_map[data['amount']] < amount_map[amount]:
                increment = -1
            elif amount_map[data['amount']] > amount_map[amount]:
                increment = 1
            else:
                increment = 0
        query = f'INSERT INTO location{location_id} (time, amount, increment)'
        query += f" VALUES (\'{data['time']}\', \'{data['amount']}\', {increment});"
        self.cursor.execute(query)
        self.db.commit()

    def get_location_data(self, location_id):
        self.db.commit()
        query = f'SELECT * FROM location{location_id};'
        self.cursor.execute(query)
        result = {'sightings': []}
        for row in self.cursor:
            sighting = {'time': row[1], 'amount': row[2], 'increment': row[3]}
            result['sightings'].append(sighting)
        return result
