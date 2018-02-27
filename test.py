import sys
import requests
import json
import time

offset = 590185715
logger = open('data/%s.log' % (time.strftime("%Y%m%d", time.localtime())), 'a', buffering=0)
while True:
    try:
        r = requests.get('https://api.telegram.org/%s/getupdates?offset=%s' % offset, timeout=10)
        update_id = 0
        for _ in r.json().get('result', []):
            update_id = _['update_id']
            #print json.dumps(_, ensure_ascii=False)
            logger.write(json.dumps(_) + '\n')
        if update_id != 0:
            offset = update_id + 1
        #print '.'
    except Exception as e:
        print e
    time.sleep(5)
