import os
import requests

API_KEY = os.environ["FINNHUB_API_KEY"]
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

stocks = ["AAPL", "NVDA", "TSLA"]

message = "📈 Stock Update\n\n"

for symbol in stocks:
    data = requests.get(
        f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
    ).json()

    price = data.get("c", "N/A")
    change = data.get("dp", "N/A")

    message += f"{symbol}: ${price} ({change}%)\n"

requests.post(
    WEBHOOK,
    json={"content": message}
)
