import sys
import time
import simplejson as json


token2id = {}
for line in sys.stdin:
    line = json.loads(line.strip())
    if 'encrypted' not in line:
        continue
    inviter_token = line.get('inviter')
    self_id = line.get('code')
    token = line.get('encrypted')
    try:
        tm = line.get('time')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.mktime(time.strptime(tm, '%Y-%m-%dT%H:%M:%S.%fZ')) + 8*3600))
    except:
        tm = ''
    token2id[token] = {'inviter_token': inviter_token, 'self_id': self_id, 'click_time': tm}

print json.dumps(token2id)
