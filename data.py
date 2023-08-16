import requests

URL = 'https://opentdb.com/api.php?amount=10&type=boolean'

#------------Api calls------------#
api_end_point_call_data = requests.get(url=URL)
api_end_point_call_data.raise_for_status()
question_data = api_end_point_call_data.json()['results']


