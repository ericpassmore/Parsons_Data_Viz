import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://www.google.com/finance/quote/MSFT:NASDAQ"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Locate table
table = soup.find("table", class_="slpEwd")
rows = table.find_all("tr")

data = {}

# 1. Extract Fiscal Period
first_row_span = rows[0].find("span")
tooltip_div = first_row_span.find("div") if first_row_span else None
tooltip_text = tooltip_div.get_text(strip=True) if tooltip_div else ""

match = re.search(r"Fiscal\s(Q[1-4]\s\d{4})\sended\s([\d/]+)", tooltip_text)
if match:
    fiscal_quarter, fiscal_date = match.groups()
    data["Period"] = [fiscal_quarter, fiscal_date]
else:
    data["Period"] = ["", ""]

# 2. Operating Income
operating_row = rows[2].find_all("td")
data["Operating Income"] = [
    operating_row[1].get_text(strip=True),
    operating_row[2].get_text(strip=True)
]

# 3. Net Income
net_row = rows[3].find_all("td")
data["Net Income"] = [
    net_row[1].get_text(strip=True),
    net_row[2].get_text(strip=True)
]

# 4. Net Profit Margin
npm_row = rows[4].find_all("td")
npm_value = npm_row[1].get_text(strip=True)
npm_pct = npm_row[2].get_text(strip=True)
if not npm_value.endswith('%'):
    try:
        val = float(npm_value)
        npm_value = f"{val:.2f}%"
    except:
        pass
data["Net Profit Margin"] = [npm_value, npm_pct]

# 5. EBITDA
ebitda_row = rows[6].find_all("td")
data["EBITDA"] = [
    ebitda_row[1].get_text(strip=True),
    ebitda_row[2].get_text(strip=True)
]

# Convert to DataFrame
rows_out = []
for metric, values in data.items():
    if len(values) == 2:
        rows_out.append([metric, values[0], values[1]])
    else:
        rows_out.append([metric] + values + [""])

df = pd.DataFrame(rows_out, columns=["Metric", "Value", "Percentage Change"])
df.to_csv("output_metrics.csv", index=False)

print("✅ Extracted financial metrics saved to 'output_metrics.csv'")
