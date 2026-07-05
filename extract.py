import requests
import init
import json
from pathlib import Path
from datetime import datetime


#Prepare url for requesting
params = {'start_date':init.date_begin, 'end_date':init.date_end, 'api_key':init.api_key}
url = init.url
#Making a request
r = requests.get(url, params=params)

#Obtaining json-file and cleaning
request_dict = r.json()
for asteroids in request_dict["near_earth_objects"].values():
    for asteroid in asteroids:
        asteroid.pop('links',None)
        asteroid.pop("neo_reference_id",None)
        asteroid.pop("nasa_jpl_url",None)
        asteroid['orbiting_body'] = asteroid["close_approach_data"][0]['orbiting_body']
        asteroid['relative_velocity_km_s'] = asteroid["close_approach_data"][0]['relative_velocity']['kilometers_per_second']
        asteroid['miss_distance_km'] = asteroid["close_approach_data"][0]['miss_distance']['kilometers']
        asteroid['miss_distance_astr'] = asteroid["close_approach_data"][0]['miss_distance']['astronomical']
        asteroid['close_approach_data'] = asteroid["close_approach_data"][0]['close_approach_date']
        asteroid['size_meter_min'] = asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"]
        asteroid['size_meter_max'] = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]
        asteroid.pop("estimated_diameter",None)

json_string = json.dumps(request_dict["near_earth_objects"], indent=4, ensure_ascii=False)

#writing json data 
path = Path(f'/home/He1ioz/Документы/python/NeoWs/ignore/raw data from {datetime.now()}.json')
path.write_text(json_string)

#MAking simple log-file
logging_path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/logs.txt')
with logging_path.open('a') as logger :
            logger.write(f'return code: {r.status_code}  total asteroids: {request_dict["element_count"]}    extract date {datetime.now()}')

