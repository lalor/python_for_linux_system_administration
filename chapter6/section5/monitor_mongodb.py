from __future__ import print_function
import pymongo
client = pymongo.MongoClient(host='127.0.0.1:27017')
client.admin.authenticate('laimingxing', 'laimingxing')
rs = client.admin.command('replSetGetStatus')

print("set:", rs['set'])
print("myState:", rs['myState'])
print("num of members:", len(rs['members']))
