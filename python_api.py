import requests

name = input("Enter any Name to predict which Country possible\n")
response = requests.get("https://api.nationalize.io/?name="+name)

l = response.json()['country']

for data in l:
    print(f"Country Code in Short: {data['country_id']} and probability: {data['probability']}")