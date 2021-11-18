import requests

def thailand_province():
    response = requests.get('https://thaiaddressapi-thaikub.herokuapp.com/v1/thailand/provinces/')
    if response.status_code == 200:
        response_json = response.json()
        return response_json['data']
