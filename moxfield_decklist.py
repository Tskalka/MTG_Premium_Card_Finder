import cloudscraper
import time
import random

def wait():
    time.sleep(random.uniform(0.05, 0.1))
    
deck_list = "-GQxUZ0aDEOzgySiXUj_VQ"

def get_decklist(deck_list):
    wait()
    scraper = cloudscraper.create_scraper()  # This handles cookies and JavaScript
    response = scraper.get(f"https://api.moxfield.com/v2/decks/all/{deck_list}")
    return response.text

print(get_decklist(deck_list))

#Now we can start iterating through the decklist to then search for the premium cards