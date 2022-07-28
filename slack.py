import os
import sys
import requests
import json
from datetime import datetime
import argparse

now = datetime.now()

parser = argparse.ArgumentParser()
parser.add_argument('--nodename')
parser.add_argument('--incidentmessage')
args = parser.parse_args()
node_name = args.nodename
incident_message = args.incidentmessage

url = os.environ["WEBHOOK_URL"]
channel_name = '#nnmi'
event_message = node_name + ': ' + incident_message

payload_dic = {
    "text":event_message,
    "username":'NNMi Message',
    "channel":channel_name
    }

payload=json.dumps(payload_dic)

def main():
    message=requests.post(url, data=payload)
    print(now, message)

if __name__ == "__main__":
    main()
