import json
import os
from datetime import datetime

data = {
    "symbol": "VOTE",
    "addresses": []
}

address_set = set() 

with open(os.path.join(os.getcwd(), "raw", "2022_May_17_snapshot", "auctions_per_creator.txt")) as f:
    lines = f.readlines()
    for line in lines:
        if line[0:2] == "\\x":
            address_set.add("0x" + line[2:].strip())

with open(os.path.join(os.getcwd(), "raw", "2022_May_17_snapshot", "campaigns_created_by_buyer.txt")) as f:
    lines = f.readlines()
    for line in lines:
        if line[0:2] == "\\x":
            address_set.add("0x" + line[2:].strip())

data["addresses"] = list(address_set)
data["addresses"].sort()

date_time = datetime.now().strftime("%Y_%b_%-d")
with open(os.path.join("whitelist", f"{date_time}_whitelist.json"), "w") as f:
    json.dump(data, f, indent=2)