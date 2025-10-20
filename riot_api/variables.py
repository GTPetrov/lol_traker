import os
import requests
from dotenv import load_dotenv

load_dotenv()

#conts
RIOT_API_KEY = os.getenv("RIOT_API")

SERVER_ID_MAP = {
    # EUROPA
    "eune": "eun1", 
    "euw": "euw1",
    "ru": "ru",
    "tr": "tr1",

    # AMERYKI
    "na1": "na1",
    "na": "na1",  # Dodatkowe zabezpieczenie
    "br1": "br1",
    "lan1": "la1",
    "las1": "la2",

    # AZJA/PACIFIK (Wymaga sprawdzenia, jeśli używasz tych starych/nowych kluczy)
    "kr": "kr",
    "jp": "jp1",
    "oce": "oc1",  # Oceania

    # PŁD.-WSCH. AZJA
    "ph": "ph2",
    "sg": "sg2",
    "th": "th2",
    "tw": "tw2",
    "vn": "vn2",
}

REGIONAL_ROUTING = {
        # Europe
        "eune": "europe", "euw": "europe", "ru": "europe", "tr": "europe", 
        # Americas
        "na1": "americas", "na": "americas", "br1": "americas", "br": "americas", 
        "lan1": "americas", "lan": "americas", "las1": "americas", "las": "americas",
        # Asia
        "kr": "asia", "jp": "asia", 
        # SEA (Southeast Asia)
        "oce": "sea", "ph": "sea", "sg": "sea", "th": "sea", "tw": "sea", "vn": "sea", 
    }


#Getting data of a player 
def get_player_data(gameName, tagLine, region_input):
    if not region_input:
        print("Błąd: Region nie został podany.")
        return None
        
    region_key = region_input.lower()

    region_route = REGIONAL_ROUTING.get(region_key)

    url = f"https://{region_route}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}/?api_key={RIOT_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd API: {response.status_code} - {response.text}")
        return None

#getting server data
def server_data(puuid, region_input):
    if not region_input:
        print("Błąd: Region nie został podany.")
        return None
        
    region_key = region_input.lower()

    region_route = REGIONAL_ROUTING.get(region_key)

    url=f"https://{region_route}.api.riotgames.com/riot/account/v1/region/by-game/lol/by-puuid/{puuid}?api_key={RIOT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd API: {response.status_code} - {response.text}")
        return None
    
#getting rank data
def get_rank(puuid,region_input):
    if not region_input:
        print("Błąd: No region chosen.")
        return None
        
    region_key = region_input.lower()
    server_id = SERVER_ID_MAP.get(region_key)

    url=f"https://{server_id}.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}?api_key={RIOT_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        full_rank = response.json()

        if not full_rank:
            #player has no rank
            tier={"tier": "UNRANKED", "rank": "", "queueType": "UNRANKED"}
            return tier
        for entry in full_rank:
            if entry.get("queueType") == "RANKED_SOLO_5x5":
                return entry
        #if no solo rank return any rank
        return full_rank[0]
    
    else:
        print(f"Błąd API: {response.status_code} - {response.text}")
        return None