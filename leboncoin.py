import requests
from datetime import datetime, timedelta

def fetch_listings(cfg):
    """Interroge l’endpoint Leboncoin et renvoie la liste brute."""
    url = "https://api.leboncoin.fr/finder/search"
    params = {
        "keywords": " ".join(cfg["keywords"]),
        "locations": [{"department": cfg["department"], "radius": cfg["radius_km"]}],
        "price": {"min": cfg["price_min"], "max": cfg["price_max"]}
    }
    resp = requests.post(url, json=params)
    return resp.json()["ads"]

def filter_listings(ads, max_age_hours):
    now = datetime.utcnow()
    res = []
    for ad in ads:
        ad_date = datetime.fromisoformat(ad["first_publication_date"].rstrip("Z"))
        if now - ad_date < timedelta(hours=max_age_hours):
            res.append(ad)
    return res
