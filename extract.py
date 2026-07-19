import requests
import init
import json
from pathlib import Path
from datetime import datetime
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

s = 15

#Prepare url for requesting
params = {'start_date':init.date_begin, 'end_date':init.date_end, 'api_key':init.api_key}
url = init.url

#Making a request with checking for return code
for _ in range(6):
    #Making a request
    r = requests.get(url, params=params, timeout= (s-5))
    if (r.status_code // 100) != 4: break
    time.sleep(s)
    logger.error(f"return code: {r.status_code}  Trying to reconnect in {s} seconds")

if 200 <= r.status_code < 300: 
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
    path = init.home/'ignore'/f'temp.json'
    path.write_text(json_string)

    #Making log note
    logger.info(f'return code: {r.status_code}  total asteroids: {request_dict["element_count"]}')

if 300 <= r.status_code < 400: logger.error(f"return code: {r.status_code}  Requested source is redirected")
if 400 <= r.status_code < 500: logger.error(f"return code: {r.status_code}  Requested source is blocked in your county")
if 500 <= r.status_code: logger.error(f"return code: {r.status_code}  Error on Server")

