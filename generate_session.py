"""
Run this LOCALLY on your machine BEFORE deploying.
It will ask you to log into Telegram, then print your session string.
Copy that string and add it as the TELEGRAM_SESSION env var on Railway.
"""
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 27801031
api_hash = "d034f95686c59270db5e97515b3da014"

# Use a throwaway name — this just generates the string
client = TelegramClient("temp_session", api_id, api_hash)
client.start()  # Will prompt you to enter your phone number + OTP

session_string = client.export_session_string()

print("\n" + "=" * 60)
print("YOUR SESSION STRING (copy everything between the quotes):")
print("=" * 60)
print(f'"{session_string}"')
print("=" * 60 + "\n")

client.disconnect()