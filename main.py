import requests
from colorama import Fore
from datetime import datetime, timezone
import json
import pprint

"""

Project Name: OSRS Item Lookup
Author: DaRealDSA @ GitHub
Current version: v0.1.1

"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

"""
Gets the latest high and low prices for the items that we have data for, 
and the Unix timestamp when that transaction took place.
"""

prices_api = requests.get(
    "https://prices.runescape.wiki/api/v2/osrs/latest", headers=headers
)
# Mapping
mapping_api = requests.get(
    "https://prices.runescape.wiki/api/v2/osrs/mapping", headers=headers
)

json_price_content_data: dict = prices_api.json()
json_mapping_content_data: dict = mapping_api.json()


# Checks if API is reaching the server for both prices and mapping
def VerifyConnection(prices_api, mapping_api):
    return prices_api.status_code == 200 and mapping_api.status_code == 200


# Converts from timestamp into readable time and returns time elapse of since purchased
def TStoTime(ts):
    dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc)

    time_delta = datetime.now(timezone.utc) - dt_utc
    minutes_since_purchase = int((time_delta.total_seconds() % 3600) // 60)
    hours_since_purchase = int(time_delta.total_seconds() // 3600)

    if hours_since_purchase == 0:
        return minutes_since_purchase
    else:
        return "%d hours and %d" % (hours_since_purchase, minutes_since_purchase)


def PriceAPISearch(id: int):
    str_id = str(id)

    # Searches through item database
    for data in json_price_content_data.values():
        item_data = data[str_id]
        # Grabs timestamp from API
        ts_api = item_data["highTime"]

        # Converts timestamp into actual time
        min_since_purchase = TStoTime(ts_api)

        # Display item info
        print(f'High value: {item_data["high"]}')
        print(f'Low value: {item_data["low"]}')
        print(f'Margin: {item_data["high"] - data[str_id]["low"]}')
        print(f"Purchased {min_since_purchase} minutes ago by a player")


def Main():
    # If item is found in mapping DB changes to True
    is_item_found = False

    # Item id place holder changes all the time until found by mapping DB
    temp_id: int = 0

    # Checks if connection is established to API mapping server
    if VerifyConnection(prices_api, mapping_api):
        print("===== OSRS ITEM LOOKUP =====")
        item_name = input("Enter item name: ")

        # Loops through JSON dict-styled data until if item_name is same
        for item in json_mapping_content_data:
            temp_id = item["id"]
            # Name matched if item is identical to user
            if item["name"].lower() == item_name.lower():
                is_item_found = True
                break

        # Item found so
        if is_item_found:
            print("Item Found: \n")
            PriceAPISearch(temp_id)
        else:
            print("Item not found, try again please")
            temp_id = 0

    else:
        print("Please check your internet connection")
        print(f"API Status code: {prices_api.status_code}")
        print(f"Mapping Status code: {mapping_api.status_code}")


# Runs this main.py directly
if __name__ == "__main__":
    Main()
