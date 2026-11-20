from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.text import Text
import sys

try:
    symbol = input("Enter your stock SYMBOL(e.g., MEBL, HBL etc.): ").upper()

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

# Find Open
label = soup.find("div", class_="stats_label", string="Open")
stats_value = label.find_next_sibling("div", class_="stats_value")
open_price = stats_value.get_text(strip=True)
print("Open:", open_price)

# Find Low
label = soup.find("div", class_="stats_label", string="Low")
stats_value = label.find_next_sibling("div", class_="stats_value")
low_price = stats_value.get_text(strip=True)
print("Low:", low_price)

# Find volume
label = soup.find("div", class_="stats_label", string="Volume")
stats_value = label.find_next_sibling("div", class_="stats_value")
volume = stats_value.get_text(strip=True)
print("Volume:", volume)

# Find ask price
label = soup.find("div", class_="stats_label", string="Ask Price")
stats_value = label.find_next_sibling("div", class_="stats_value")
ask_price = stats_value.get_text(strip=True)
print("Ask Price:", ask_price)

# Find current price
label = soup.find("div", class_="quote__close")
current_price = label.get_text(strip=True)
print("Current Price:", current_price)

# Change value
label = soup.find("div", class_="change__value")
change_value = label.get_text(strip=True)
if "-" in change_value:
    change_value = "▼" + change_value
else:
    change_value = "▲" + change_value
print("Change Value:", change_value)

# Change percent
label = soup.find("div", class_="change__percent")
change_percent = label.get_text(strip=True)
print("Change Percent:", change_percent)

# Table using rich
table = Table(title=soup.title.text, min_width=70)
table.add_column("Retrieval Time", justify="center", style="grey42")
table.add_column("Open", justify="center", style="grey11")
table.add_column("Low", justify="center", style="grey11")
table.add_column("Volume", justify="center", style="grey11")
table.add_row(fetch_date, str(open_price), str(low_price), str(volume))
# Print Table
console = Console()
console.print(table)

# Bidding table
table = Table(title="Bidding Information", min_width=70)

# Showing green or red color for change value and percentage
if "-" in change_value:
    price_change = Text(current_price)
    price_change.append(f" {change_value}{change_percent}", style="red")
    table.add_column("Current Price", justify="center", style="grey11")
else:
    price_change = Text(current_price)
    price_change.append(f" {change_value}{change_percent}", style="green")
    table.add_column("Current Price", justify="center", style="grey11")

table.add_column("Ask Price", justify="center", style="cyan")
table.add_row(price_change, ask_price)
# Print Table
console = Console()
console.print(table)
