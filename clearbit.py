import requests
import json
def get_clearbit_data(email):
    url = f"https://person.clearbit.com/v2/combined/find?email=davortelisman"
    response = requests.get(url)
    if response.status_code == 200:
        # If the request is successful (status code 200), you can work with the response data
        data = response.json()
        # Do something with the data
        print(data)
    else:
        # If there was an error with the request, print the status code and any error message
        print(f"Request failed with status code {response.status_code}: {response.text}")