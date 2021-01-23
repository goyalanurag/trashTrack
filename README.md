# Trash-Track

Geo Tracking of littered garbage, triggering alerts and mapping areas with high waste index.

### Backend
* Images are collected by cameras installed on public vehicles.
* Machine learning model analyzes for the amount of garbage (low/medium/high).
* Geolocation coordinates are maaped to a location cluster.

### Web application
* Fetches district-specific data from database and projects the locations on a map.
* Graphical analysis of time-based trend of garbage amount at specific locations.


in `frontend` run:
* `npm install`
* `npm start`

in `backend` run:
* `python3 routes.py`
