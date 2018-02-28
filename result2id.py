import sys
import simplejson as json
from config import project

result = {}
teleid2result = json.loads(open(project + '/teleid2result.json', 'rb').read())
for teleid, value in teleid2result.items():
    self_id = value['self_id']
    inviter_id = value['inviter_id']
    if self_id not in result:
        result[self_id] = {'self': 1, 'share': 0, 'self_info': value, 'share_info_list': []}
    if inviter_id not in result:
        result[inviter_id] = {'self': 0, 'share': 1, 'self_info': {}, 'share_info_list': [value]}
    else:
        result[inviter_id]['share'] += 1
        result[inviter_id]['share_info_list'].append(value)
print json.dumps(result)
