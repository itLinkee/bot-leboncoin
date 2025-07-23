# main.py
from config import SEARCH, CREDENTIALS, CALLBACK_SLOTS
from leboncoin import fetch_listings, filter_listings
from message import render_message
from send import send_message

ads = fetch_listings(SEARCH)
fresh_ads = filter_listings(ads, SEARCH["max_age_hours"])
for ad in fresh_ads:
    msg = render_message(ad, CALLBACK_SLOTS)
    send_message(ad["url"], msg, CREDENTIALS)
