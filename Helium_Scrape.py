import requests

def check_status():
    #The url needs your miners address. This can be found on the explorer page, and is the string followed
    #by the "@" symb
    url = "https://api.helium.io/v1/hotspots/INSERT_YOUR_ADDRESS_HERE
    #Example
    #url = "https://api.helium.io/v1/hotspots/112Axn3a3kDZFkuWgbQTsNvwPH7eK8iM3RBrMwGVxiPT9YK6hDt4"
    r = requests.get(url)

    json_data = r.json()
    status = json_data['data']['status']['online']
    return status





