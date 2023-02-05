from natgeo import *
import pymongo
import argparse



def access_db():
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    articles = get_natgeo()
    
    db = client["natgeo-db"]
    coll = db["natgeo-coll"]

    for a in articles:  
        if a not in coll.find(a, {'_id': 0}):
            try:
                coll.insert_one(a)
            except:
                print('fail to insert')
    return coll

# for i in coll.find({}, {"_id":0}):
#     print(i)
# coll.drop()
# print(coll.count_documents({}))

def list_dbs():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    dbs = list(client.list_database_names())
    for db in dbs[3:]:
        print(db)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='list all databases', action='store_true')
    args = parser.parse_args()
    
    if args.list:
        list_dbs()
    access_db()
