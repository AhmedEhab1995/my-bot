import nest_asyncio
import asyncio
from telethon.sync import TelegramClient
from telethon import events
import requests

# Patch the event loop for Spyder
nest_asyncio.apply()

# Telegram API credentials
api_id = "27801031"
api_hash = "d034f95686c59270db5e97515b3da014"

# Slack Webhook URL
SLACK_WEBHOOK = "https://hooks.slack.com/services/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"

import os 
os.environ["TELETHON_NO_CONNECTION_RETRIES"] = "1"

client = TelegramClient('gold_session_listener', api_id, api_hash)

# Listen to multiple channels
@client.on(events.NewMessage(chats=['OffersEgyptofficial', 'Sal7lyEgypt', 'Yo_Ayman', 'Reviewhk', 'deals_me', 'Sal7lySaudi', 'Sal7lyEmirates', 'Mego_Reviews', 'OffersEgyptofficial', 'Sal7lyMAIN', 'EshterySa7', 'Final_Offers']))
async def handler(event):
    message = event.message.message
     
    # Get the channel name
    chat = await event.get_chat()
    channel_name = chat.username if chat.username else chat.title
    
    # Format message with channel name
    formatted_message = f"📢 **{channel_name}**\n\n{message}"
    
    print(f"Received from {channel_name}: {message}")
    
    try:
        # Send to Slack
        response = requests.post(SLACK_WEBHOOK, json={"text": formatted_message})
        if response.status_code == 200:
            print(f"✅ Sent to Slack from {channel_name}")
        else:
            print(f"❌ Failed to send. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending to Slack: {e}")

async def main():
    await client.start()
    print("Listening to 11 channels and forwarding to Slack...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())