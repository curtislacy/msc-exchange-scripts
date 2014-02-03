#get balance
import sys
import json

if sys.argv[1] == '-h' or sys.argv[1] == '--help': 
    print "\nTakes a list of MSC addresses in and outputs the balance\nUsage: cat listOfAddresses.json | getBalanceMSC.py\nRequires a fully-synced omniwallet node"
    exit()

tmp='/tmp/omniwallet/addr/'    

JSON = sys.stdin.readlines()

listAddresses = json.loads(str(''.join(JSON)))
results = []
for addr in listAddresses['addresses']:
    try:
        f=open(tmp + addr + '.json')
        address = json.loads(f.readline())
        results.append({ 'address': address['address'], 'balance': address['balance']})
    except IOError:
        print "No such MSC address " + addr

print json.dumps(results)
