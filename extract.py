import requests
import init
import json
from pathlib import Path


#Prepare url for requesting
params = {'start_date':init.date_begin, 'end_date':init.date_end, 'api_key':init.api_key}
url = init.url
#Making a request
r = requests.get(url, params=params)

#Obtaining json-file and cleaning it from links containing astroid data during date_begin and date_end from init.py-file
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

        '''for dates in asteroid["close_approach_data"]:
            dates.pop("close_approach_date_full",None)
            dates.pop("epoch_date_close_approach",None)
            dates.pop("miles_per_hour",None)
            dates['relative_velocity'].pop('kilometers_per_hour',None)
            dates['relative_velocity'].pop('miles_per_hour',None)
            dates['miss_distance'].pop('lunar',None)
            dates['miss_distance'].pop('miles',None)'''


json_string = json.dumps(request_dict["near_earth_objects"], indent=4, ensure_ascii=False)

#writing json data 
path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/temp.json')
path.write_text(json_string)

#MAking simple log-file
logging_path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/logs.txt')
logging_path.write_text(f'return code: {r.status_code}  total asteroids: {request_dict["element_count"]}')

