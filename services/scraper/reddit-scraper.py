import time
import httpx
import pandas as pd

# creates a csv containing data of reddit posts from selected subreddit and category

base_url = 'https://www.reddit.com'
subreddit = '/r/creepypasta'
category = '/hot'

url = base_url + subreddit + category + '.json'
after_post_id = None
dataset = []

for i in range(1):
    params = {
        'limit' : 25,
        't' : 'year',
        'after' : after_post_id
    }
    response = httpx.get(url, params=params)
    print(f'Fetching data from {response.url}')
    if response.status_code != 200:
        raise Exception('Failed to fetch data')
    
    json_data = response.json()

    dataset.extend(rec['data'] for rec in json_data['data']['children'])

    after_post_id = json_data['data']['after']
    time.sleep(0.5)
    print(json_data['data']['children'][0]['data'].keys())
    

df = pd.DataFrame(dataset)
df.to_csv('reddit_python.csv', index=False)

