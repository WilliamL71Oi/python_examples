from ipwhois import IPWhois
import json


obj = IPWhois('114.114.114.114')
results = obj.lookup_rdap(asn_methods=["whois"])
print(json.dumps(results, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False))
