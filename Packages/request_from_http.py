import pprint
import requests

r = requests.get('https://api.dailysmarty.com/posts')
pprint.pprint(r.json()['posts'][0]['url_for_post'])
