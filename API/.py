import requests

# Joke API endpoint

url = "https://official-joke-api.appspot.com/random_joke"

# Send GET request to fetch a joke

response = requests.get(url)

# Check if the request was successful

if response.status_code == 200:

    joke_data = response.json()

    print(f"Joke: {joke_data['setup']} - {joke_data['punchline']}")

else:

    print("Failed to retrieve joke")