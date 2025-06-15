import requests as r
import time
import random

def wait():
    time.sleep(random.uniform(0.05, 0.1))

def find_premium_card(card_name):

    #Get's the card's prints_search_uri
    wait()
    scryfall_url = f"https://api.scryfall.com/cards/named?exact={card_name}"
    card_data = r.get(scryfall_url).json()

    #Get's the specific printings 
    prints_search_uri = card_data["prints_search_uri"]
    wait()
    prints_search_data = r.get(prints_search_uri).json()["data"]

    #Now we'll want to check which of all the prices is highest, usd
    highest_price = 0
    for card in prints_search_data:
        if(card["prices"]["usd"] is not None):
            if(float(card["prices"]["usd"]) > highest_price):
                highest_price = float(card["prices"]["usd"])
                card_with_highest_price = card
            
        if(card["prices"]["usd_foil"] is not None):
                if(float(card["prices"]["usd_foil"]) > highest_price):
                    highest_price = float(card["prices"]["usd_foil"])
                    card_with_highest_price = card

        if(card["prices"]["usd_etched"] is not None):
            if(float(card["prices"]["usd_etched"]) > highest_price):
                highest_price = float(card["prices"]["usd_etched"])
                card_with_highest_price = card

    return card_with_highest_price["id"]


print(find_premium_card("Hazel of the Rootbloom"))