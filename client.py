import os
import argparse

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

parser = argparse.ArgumentParser("client.py")
parser.add_argument("target_address", help="IP address of the Huawei router")
parser.add_argument("password", help="Admin user password.")
args = parser.parse_args()

url = "http://admin:" + args.password + "@" + args.target_address

print (url)
connection = AuthorizedConnection(url)
client = Client(connection)

print(client.device.signal())  # Can be accessed without authorization
print(client.device.information())  # Needs valid authorization, will throw exception if invalid credentials are passed in URL


# For more API calls just look on code in the huawei_lte_api/api folder, there is no separate DOC yet