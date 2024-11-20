import requests
import time

def get_region_by_coordinates(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    try:
        response = requests.get(url, timeout=10) 
        if response.status_code == 200:
            data = response.json()
            province = data.get("address", {}).get("state", "Unknown")
            time.sleep(1) 
            return province.upper()
        else:
            print(f"Error: {response.status_code}")
            time.sleep(1)  
            return "Unknown"
    except Exception as e:
        print(f"Exception occurred: {e}")
        time.sleep(1)  
        return "Unknown"



