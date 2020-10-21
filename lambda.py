from datetime import datetime
import json
import urllib.request

def lambda_handler(event, context):
    ''' Demonstrates a simple HTTP request from Lambda '''
    #item_response = urllib.request.urlopen(base_url)
    #response_string = item_response.read().decode('utf-8')
    #item = json.loads(response_string)
    base_url = 'https://hacker-news.firebaseio.com/v0/item/'
    answer = []
    for itemid in range(1, 10):
    # Get item
        item_response = urllib.request.urlopen(base_url + str(itemid) + '.json')
        response_string = item_response.read().decode('utf-8')
        item = json.loads(response_string)
        time = item['time']
        ts = int(time)
        ans = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        answer.append(ans)
    #now = datetime.now()
    #current_time = now.strftime("'%Y-%m-%d %H:%M:%S'")
    #time = item['time']
    #ts = int(time)
    #ans = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return answer