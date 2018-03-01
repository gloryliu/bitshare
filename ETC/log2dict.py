import sys
import simplejson as json


token2id = {}
for line in sys.stdin:
    line = json.loads(line.strip())
    if 'encrypted' not in line:
        continue
    inviter_token = line.get('inviter')
    self_id = line.get('code')
    token = line.get('encrypted')
    time = line.get('time').replace('T', ' ').replace('Z', '')
    token2id[token] = {'inviter_token': inviter_token, 'self_id': self_id, 'click_time': time}

print json.dumps(token2id)
