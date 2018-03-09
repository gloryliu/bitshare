# encoding=utf8
import os
import sys
import json
import time
import requests
from config import project

token = os.environ['TOKEN']
print 'TOKEN:', token
offset = int(open('let.offset', 'rb').read())
while True:
    try:
        logger = open(project + '/data/%s.log' % (time.strftime("%Y%m%d", time.localtime())), 'r')
    except Exception as e:
        time.sleep(30)
        continue
    push_list = []
    for line in logger:
        try:
            line = json.loads(line)
            message = line['message']['text']
            update_id = line['update_id']
            if len(message) != 32:
                continue
            if update_id > offset:
                push_list.append(message)
                offset = update_id 
        except Exception as e:
            continue
    logger.close()
    print '.....'
    if push_list == []:
        time.sleep(10)
        continue
    s = u'comfirmed user\n已确认用户\n%s\nLET to be given out within 7 working days after the event!\nLET将会在活动结束后7个工作日内发放到Huobi.Pro账户！' % ('\n'.join(push_list))
    open('let.offset', 'wb').write(str(offset))
    try:
        url = 'https://api.telegram.org/bot%s/sendMessage' % (token)
        data = {
            'chat_id': '-1001253903979',
            'text': s,
        }
        r = requests.post(url, timeout=10, data=data)
        print r.json()
    except Exception as e:
        print e
    time.sleep(10)
