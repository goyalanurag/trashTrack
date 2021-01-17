def clustering(coordinates, postcode):
    location = coordinates.split(',')
    location = [float(n.strip()) for n in location]
    location = [int(10000*n)/10000 for n in  location]
    location = [str(n) for n in location]
    location = ','.join(location)

    return location
