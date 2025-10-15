import os
import requests
from dotenv import load_dotenv

load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API")

#Getting data of a player 

#dodaj by region się wybierało nastronce
def get_player_data(gameName, tagLine):
    url=f"https://eun1.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    headers = {"Riot_key": RIOT_API_KEY}
    response = requests.get(url, headers=headers)

    if response == 200:
        return response.json()
    else:
        print("{response.text}")
        return None