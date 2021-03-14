"""
Client wrapper for huawei-lte-api for basic control of a 5g router.
"""
import argparse
import json

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection

PARSER = argparse.ArgumentParser("client.py")
PARSER.add_argument("target_address", help="IP address of the Huawei router")
PARSER.add_argument("password", help="Admin user password.")
PARSER.add_argument("--signal", dest="signal",
                    action="store_true", help="Signal status.", required=False)
PARSER.add_argument("--info", dest="info",
                    action="store_true", help="Device info.", required=False)
PARSER.add_argument("--bands", dest="bands",
                    action="store_true",
                    help="Lock router to LTE bands supplied here.",
                    required=False)
PARSER.add_argument("--reboot", dest="reboot",
                    action="store_true",
                    help="Reboot router.",
                    required=False)
ARGS = PARSER.parse_args()

URL = "http://admin:" + ARGS.password + "@" + ARGS.target_address

CONNECTION = AuthorizedConnection(URL)
CLIENT = Client(CONNECTION)

# Check which info to display
if ARGS.signal:
    print("Signal status:")
    print(json.dumps(CLIENT.device.signal(), indent=5))
    print("")
if ARGS.info:
    print("Device information:")
    print(json.dumps(CLIENT.device.information(), indent=5))
    print("")

# Check if we are going to change the bands
if ARGS.bands:
    print("Changing LTE bands.....")
    # Set band
    try :
        networkband = "3FFFFFFF"
        networkmode = "00"
        lteband="3FFFFFFF"
        CLIENT.net.set_net_mode(lteband, networkband, networkmode) 

    except Exception as e :
        print("Connection error - " + str(e))
        exit()

# Check if we should reboot the router
if ARGS.reboot:
    print("Rebooting the router.....")
    try :
        CLIENT.device.reboot()

    except Exception as e :
        print("Connection error - " + str(e))
        exit()
    
