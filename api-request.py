import requests

api_key = "14da182bfb45e54860f3c5bcdcaf4250"
base_url = "http://api.weatherstack.com/current"

params = {
    "access_key": api_key,
    "query": "California"
}

def fetch_data():
    print("Fetching Data from the Weather-Stack-API")
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestsException as e:
        print(f"An error occured: {e}")
        raise
        
fetch_data()

# api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"