import pandas as pd
from pathlib import Path
import json


path = Path('/home/He1ioz/Документы/python/NeoWs/ignore/temp.json')
data = json.loads(path.read_text())

my_data=pd.DataFrame(data["2015-09-07"])

df = pd.read_json('/home/He1ioz/Документы/python/NeoWs/ignore/temp.json')

