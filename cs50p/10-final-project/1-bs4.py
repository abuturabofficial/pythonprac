from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
import sys

try:
    symbol = input("Enter your stock SYMBOL: ").upper()

    with open(f"{symbol}.html", "r") as f:
        html = f.read()
except Exception:
    sys.exit("Invalid SYMBOL name")

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())
print(soup.title.text)

# Date of printing
label = soup.find("div", class_="quote__date").get_text()

_, fetch_date = label.split("^ As of")

print("Date:", fetch_date.strip())

label = soup.find("div", class_="stats_label", string="Open")
open_price = float(
    label.find_next_sibling("div", class_="stats_value")
    .get_text(strip=True)
    .replace(",", "")
)

print("Open:", open_price)

label = soup.find("div", class_="stats_label", string="Low")
low_price = float(
    label.find_next_sibling("div", class_="stats_value")
    .get_text(strip=True)
    .replace(",", "")
)
print("Low:", low_price)

label = soup.find("div", class_="stats_label", string="Volume")
volume = float(
    label.find_next_sibling("div", class_="stats_value")
    .get_text(strip=True)
    .replace(",", "")
)
print("Volume:", volume)


# Table using rich
table = Table(title=soup.title.text, min_width=100)
table.add_column("Current Time", justify="center", style="grey42")
table.add_column("Open", justify="center", style="green")
table.add_column("Low", justify="center", style="red")
table.add_column("Volume", justify="center", style="blue")

table.add_row(fetch_date, str(open_price), str(low_price), str(volume))


console = Console()
console.print(table)
