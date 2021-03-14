import os
import argparse
import json as json

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

parser = argparse.ArgumentParser("client.py")
parser.add_argument("target_address", help="IP address of the Huawei router")
parser.add_argument("password", help="Admin user password.")
args = parser.parse_args()

url = "http://admin:" + args.password + "@" + args.target_address

connection = AuthorizedConnection(url)
client = Client(connection)

print("Signal status:")
print(json.dumps(client.device.signal(), indent=5))
print("")

print("Device information:")
print(json.dumps(client.device.information(), indent=5))


# For more API calls just look on code in the huawei_lte_api/api folder,
# there is no separate DOC yet
