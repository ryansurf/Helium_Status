import requests

def check_status():
    url = "https://api.helium.io/v1/hotspots/11CSjJtJRWK6ZT16KcRK2Hy51gMBPgLvJMAuFsEnyWgd1qwcucW"
    r = requests.get(url)

    json_data = r.json()
    status = json_data['data']['status']['online']
    return status





