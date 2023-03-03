# astoundPing
A python script to prove to Astound that my internet is having issues

You must have Astound cable internet to use this script

## Instructions

1. Head over to http://il.speedtest.astound.com/merlin/. 
2. Inspect the page and open the Network tab. Analyze what URL it is using for the ICMP request. (This should happen roughly once every sec)
3. Set that URL to the pingLink variable and run the script. Keep it running for a few hours.

Any latency above pingLimit (defaults to 100) will be written to a file in the root directory titled ping.txt. Occassional 100ms may be normal but anything consistently reaching 300-1000 show something is wrong. 

