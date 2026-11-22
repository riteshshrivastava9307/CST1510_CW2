import requests
import pandas as pd
from pathlib import Path

URL = "https://disease.sh/v3/covid-19/countries"

response = requests.get(URL, timeout=15)
response.raise_for_status()

data = response.json()

df = pd.json_normalize(data)

KEEP = [
    "country",
    "continent",
    "cases",
    "deaths",
    "population",
    "recovered"
]

df = df[KEEP]
df = df.dropna(subset=["cases", "continent"])

output = Path(__file__).parent.parent / "DATA" / "raw.csv"

output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output, index=False)

print(df.head())
print("Shape:", df.shape)
print("File saved successfully!")