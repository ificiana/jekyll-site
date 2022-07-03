import argparse
from pathlib import Path

import pymongo
import yaml

parser = argparse.ArgumentParser(description='Create data files')
parser.add_argument('mongo_username', type=str,
                    help='mongodb username')
parser.add_argument('mongo_password', type=str,
                    help='mongodb user password')
parser.add_argument('mongo_cluster', type=str,
                    help='mongodb cluster')
parser.add_argument('mongo_subdomain', type=str,
                    help='mongodb.net subdomain')

parser.add_argument('database', nargs="?", type=str,
                    help='mongodb database', default="mongo")

args = parser.parse_args()

client = pymongo.MongoClient(f"mongodb+srv://{args.mongo_username}:{args.mongo_password}@"
                             f"{args.mongo_cluster}.{args.mongo_subdomain}.mongodb.net"
                             "/?retryWrites=true&w=majority")
db = client[args.database]
for col in db.list_collection_names():
    _dir = Path("../_data/")
    print(col)
    if col != "top":
        _dir = _dir.joinpath(col)
        Path.mkdir(_dir, exist_ok=True)
    print(_dir)
    col = db[col]
    for doc in col.find():
        d = {k: v for k, v in doc.items() if k not in ("id", "_id")}
        with _dir.joinpath(f'{doc["id"]}.yml').open('w') as yaml_file:
            print(yaml_file)
            yaml.dump(d, yaml_file, default_flow_style=False)
