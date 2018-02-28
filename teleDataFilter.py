import sys
import time
import simplejson as json

token2id = json.loads(file('token2id.json', 'rb').read())
result = {}

for line in sys.stdin:
    line = json.loads(line.strip())
    if 'message' not in line:
        continue
    message = line['message']
    if 'date' not in message or 'text' not in message:
        continue
    date = message['date']
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(date)))
    text = message['text'].strip()
    if text not in token2id:
        continue
    teleid = message.get('from', {}).get('id')
    if teleid not in result or result[teleid]['tele_time'] < date:
        inviter_token = token2id[text]['inviter_token']
        inviter_info = token2id.get(inviter_token, {})
        inviter_id = inviter_info.get('self_id', '')
        inviter_click_time = inviter_info.get('click_time', '')
        result[teleid] = dict(token2id[text], **{'tele_time': date, 'self_token': text, 'inviter_id': inviter_id, 'inviter_click_time': inviter_click_time, 'teleid': teleid})

print json.dumps(result)
