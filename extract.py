import requests
import init

params = {'start_date':init.date_begin, 'end_date':init.date_end, 'api_key':init.api_key}
url = init.url

r = requests.get(url, params = params, timeout = 60)


print(r.status_code)
