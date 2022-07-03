import argparse
from pathlib import Path

import pymongo
import yaml

parser = argparse.ArgumentParser(description='Create data files')
parser.add_argument('mongo_url', type=str,
                    help='mongodb url')
parser.add_argument('database', nargs="?", type=str,
                    help='mongodb database', default="mongo")
args = parser.parse_args()

client = pymongo.MongoClient(f"{args.mongo_url}")
db = client[args.database]
for col in db.list_collection_names():
    _dir = Path("../_data/")
    if col != "top":
        _dir = _dir.joinpath(col)
        Path.mkdir(_dir, exist_ok=True)
    col = db[col]
    for doc in col.find():
        d = {k: v for k, v in doc.items() if k not in ("id", "_id")}
        with _dir.joinpath(f'{doc["id"]}.yml').open('w') as yaml_file:
            yaml.dump(d, yaml_file, default_flow_style=False)
