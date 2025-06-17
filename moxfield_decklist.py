import cloudscraper
import time
import random
import json

def wait():
    time.sleep(random.uniform(0.05, 0.1))
    
deck_list = "-GQxUZ0aDEOzgySiXUj_VQ"

def get_decklist(deck_list):
    wait()
    scraper = cloudscraper.create_scraper()  # This handles cookies and JavaScript
    response = scraper.get(f"https://api.moxfield.com/v2/decks/all/{deck_list}")
    return response.json()



# pretty = json.dumps(get_decklist(deck_list), indent=4)
# print(pretty)

#Read JSON to file
# Uncomment the following lines to save the output to a file

# with open('output.json', 'w', encoding='utf-8') as f:
#     json.dump(get_decklist(deck_list), f, indent=4, ensure_ascii=False)

