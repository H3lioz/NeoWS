import pandas as pd
from pathlib import Path
import json
import init
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Opening json-file
path = init.home/'ignore/temp.json'
data = json.loads(path.read_text())

date = init.date_begin
#Extracting data on current day
my_data=pd.DataFrame(data[date])
#Calculating avg size
size = (my_data['size_meter_min']+my_data['size_meter_max'])/2
#Making asteroid dataframe on current date
asteroid_db_cur = pd.DataFrame({'ID': my_data['id'], 'Name': my_data['name'], 'Size': size, 'Size Category': 'default', 'Magnitude': my_data['absolute_magnitude_h'], 'Latest research date': date})
asteroid_db_cur.loc[asteroid_db_cur['Size'] < 100,'Size Category'] = 'Small'
asteroid_db_cur.loc[(100 <= asteroid_db_cur['Size']) & (asteroid_db_cur['Size'] < 500),'Size Category'] = 'Medium'
asteroid_db_cur.loc[500 <= asteroid_db_cur['Size'],'Size Category'] = 'Large'


#Making dataframe with research parameters on current date
asteroid_param_cur = pd.DataFrame({'ID': my_data['id'], 'Close approach date': my_data['close_approach_data'], 'Orbiting body': my_data['orbiting_body'], 'Relative velocity, km/s': my_data['relative_velocity_km_s'], 
                                   'Miss distance, km': my_data['miss_distance_km'], 'Miss distance, ASTR': my_data['miss_distance_astr'], 'Research_date': date})



#making csv-files output
patcsv_1 = init.home/'ignore/Asteroid_DB.csv'
patcsv_2 = init.home/'ignore/Oberving_params.csv'

asteroid_db_cur.to_csv(patcsv_1,index=0)
asteroid_param_cur.to_csv(patcsv_2,index=0)

logger.info(f"Created two CSV-files")