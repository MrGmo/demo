import requests

def fetch_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

if __name__ == "__main__":
    pokemon_data = fetch_pokemon("pikachu")
    if pokemon_data:
        print(pokemon_data)
