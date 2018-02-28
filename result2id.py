import sys
import simplejson as json

result = {}
teleid2result = json.loads(open('teleid2result.json', 'rb').read())
for teleid, value in teleid2result.items():
    self_id = value['self_id']
    inviter_id = value['inviter_id']
    if self_id not in result:
        result[self_id] = {'self': 1, 'share': 0, 'self_info_list': [value], 'share_info_list': []}
    else:
        result[self_id]['self'] += 1
        result[self_id]['self_info_list'].append(value)
    if inviter_id not in result:
        result[inviter_id] = {'self': 0, 'share': 1, 'self_info_list': [], 'share_info_list': [value]}
    else:
        result[self_id]['share_info_list'].append(value)
print json.dumps(result)
