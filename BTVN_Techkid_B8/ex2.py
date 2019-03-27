from matplotlib import pyplot
from pymongo import MongoClient

# 1. Connect mongo
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(mongo_uri)

# 2. Get / Create database
dulieu = client.c4e

# 3. Get / Create collection
collections = dulieu['customers']
events = 0
wom = 0
ads = 0

all_collections = list(collections.find())

for a in all_collections :
    if a['ref'] == 'events' :
        events = events +1
    elif a['ref'] == 'wom' :
        wom = wom + 1 
    else : 
        ads = ads + 1

# 
print('events = ',events)
print('wom = ',wom)
print('ads = ',ads)     

# 
machine_counts = [events,wom,ads]
machine_names = ['Events', 'Wom', 'Ads']
pyplot.pie(machine_counts, labels=machine_names, autopct='%.1f%%', shadow=True, explode=[0,0.2,0.3])
pyplot.title("Events and Wom and Ads")
pyplot.show() 