import os
import requests
from dotenv import load_dotenv

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API")

#Getting data of a player 

def get_player_data(gameName, tagLine, region):
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}/?api_key={RIOT_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd API: {response.status_code} - {response.text}")
        return None

def server_data(puuid, region):
    url=f"https://{region}.api.riotgames.com/riot/account/v1/region/by-game/lol/by-puuid/{puuid}?api_key={RIOT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd API: {response.status_code} - {response.text}")
        return None