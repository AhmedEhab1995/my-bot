import nest_asyncio
import asyncio
import os
import requests
from telethon.sync import TelegramClient
from telethon import events
from telethon.sessions import StringSession

nest_asyncio.apply()

# --- Load secrets from environment variables ---
api_id = int(os.environ["TELEGRAM_API_ID"])
api_hash = os.environ["TELEGRAM_API_HASH"]
session_string = os.environ["TELEGRAM_SESSION"]
SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK"]

# --- Telegram client using session string (no local file needed) ---
client = TelegramClient(StringSession(session_string), api_id, api_hash)

# --- Channels to listen to ---
CHANNELS = [
    "OffersEgyptofficial",
    "Sal7lyEgypt",
    "Yo_Ayman",
    "Reviewhk",
    "deals_me",
    "Sal7lySaudi",
    "Sal7lyEmirates",
    "Mego_Reviews",
    "Sal7lyMAIN",
    "EshterySa7",
    "Final_Offers",
]

@client.on(events.NewMessage(chats=CHANNELS))
async def handler(event):
    message = event.message.message

    # Get channel name
    chat = await event.get_chat()
    channel_name = chat.username if chat.username else chat.title

    # Format message
    formatted_message = f"📢 **{channel_name}**\n\n{message}"

    print(f"Received from {channel_name}: {message}")

    try:
        response = requests.post(SLACK_WEBHOOK, json={"text": formatted_message})
        if response.status_code == 200:
            print(f"✅ Sent to Slack from {channel_name}")
        else:
            print(f"❌ Failed to send. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending to Slack: {e}")


async def main():
    await client.start()
    print("✅ Bot started. Listening to channels and forwarding to Slack...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())