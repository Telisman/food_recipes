import json
import requests
hunter ="https://api.hunter.io/v2/email-verifier?email=davortelismank@gmail.com&api_key=5daa2ca116eebcb451f0736dc888126983c3f97d"
def load(source, output_file=None):
    """Load JSON data from a file or URL"""
    if source.startswith('http'):
        response = requests.get(source)
        if response.status_code == 200:
            data = response.json()
            if output_file:
                with open(output_file, 'w') as f:
                    json.dump(data, f, indent=4)
            return data
        else:
            raise ValueError(f"Failed to fetch data from {source}. Error: {response.status_code}")
    else:
        with open(source, 'r') as file:
            return json.load(file)

email_data = load(hunter, 'hunter.json')

