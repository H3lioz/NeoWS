import requests
import init
import json
from pathlib import Path


#Prepare url for requesting
params = {'start_date':init.date_begin, 'end_date':init.date_end, 'api_key':init.api_key}
url = init.url
#Making a request
r = requests.get(url, params=params)
#Simple cleaning json-file from links
request_dict = r.json()
for asteroids in request_dict["near_earth_objects"].values():
    for asteroid in asteroids:
        asteroid.pop('links',None)
#Obtaining json-file containing astroid data during date_begin and date_end from init.py-file
json_string = json.dumps(request_dict["near_earth_objects"], indent=4, ensure_ascii=False)

#writing json data 
path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/temp.json')
path.write_text(json_string)

#MAking simple log-file
logging_path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/logs.txt')
logging_path.write_text(f'return code: {r.status_code}  total asteroids: {request_dict["element_count"]}')

