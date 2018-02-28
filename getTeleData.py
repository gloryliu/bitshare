import os
import sys
import json
import time
import requests
from config import project

token = os.environ['TOKEN']
print 'TOKEN:', token
offset = 590185715
while True:
    logger = open(project + '/data/%s.log' % (time.strftime("%Y%m%d", time.localtime())), 'a', buffering=0)
    try:
        url = 'https://api.telegram.org/bot%s/getupdates?offset=%s' % (token, offset)
        r = requests.get(url, timeout=10)
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
    logger.close()
    time.sleep(5)
