import requests
from fake_useragent import UserAgent

symbol = input("Please enter company name: ").upper()
url = f"https://dps.psx.com.pk/company/{symbol}"

session = requests.session()
headers = {
    "User-Agent": UserAgent().random,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, defalte, br, zstd",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com",
}

r = session.get(url, headers=headers)

with open(f"{symbol}.html", "w") as f:
    f.write(r.text)
