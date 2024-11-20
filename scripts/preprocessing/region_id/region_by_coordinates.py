import requests

def get_region_by_coordinates(latitude, longitude):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude},{longitude}&key={CAGE_DATA_API_KEY}&language=en&no_annotations=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['components'].get('state', 'Unknown')
    print("S4")
    return 'Unknown'

CAGE_DATA_API_KEY = "6266cf20b8754b56b454d79b4c752dd5"

