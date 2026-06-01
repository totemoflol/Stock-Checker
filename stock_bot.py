import os
import requests

API_KEY = os.environ["d8epd4pr01qub7ke2id0d8epd4pr01qub7ke2idg"]
WEBHOOK = os.environ["https://discord.com/api/webhooks/1511013946646204556/A7No3F95ccDnpwmylshL3Rftpztoey4hGvNFQJ0Lx4ZzjZmxHXRNenD0JIUfR-Q-KDBI"]

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
