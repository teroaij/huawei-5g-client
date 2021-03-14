"""
Client wrapper for huawei-lte-api for basic control of a 5g router.
"""
import argparse
import json as json

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection

PARSER = argparse.ArgumentParser("client.py")
PARSER.add_argument("target_address", help="IP address of the Huawei router")
PARSER.add_argument("password", help="Admin user password.")
PARSER.add_argument("--signal", dest="signal", action="store_true", help="Signal status.", required=False)
PARSER.add_argument("--info", dest="info", action="store_true", help="Device info.", required=False)
ARGS = PARSER.parse_args()

URL = "http://admin:" + ARGS.password + "@" + ARGS.target_address

CONNECTION = AuthorizedConnection(URL)
CLIENT = Client(CONNECTION)

# Check which info to display
if ARGS.signal:
    print("Signal status:")
    print(json.dumps(CLIENT.device.signal(), indent=5))
    print("")
elif ARGS.info:
    print("Device information:")
    print(json.dumps(CLIENT.device.information(), indent=5))
    print("")
