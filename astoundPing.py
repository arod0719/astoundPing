import datetime
import requests
import json
import time

pingLink = # Ex:'http://il.speedtest.astound.com/merlin/Widget/ping.cgi?ip=<IPADDRESS}>'
outputFile = 'ping.txt'
pingLimit = 100

while True:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    payload = json.loads(requests.get(pingLink).text)
    number = payload['ping'][0]['pingresult']
    if number and float(number) > pingLimit:
        with open(outputFile, 'a') as f:
            f.write(f'pingresult: {number} time: {timestamp}\n')
    time.sleep(0.5)
