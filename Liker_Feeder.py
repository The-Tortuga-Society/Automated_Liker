#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 14:47:10 2025

@author: wln
"""

#This program collects  messages from a Telegram channel, determines whether they have links to Substack posts, 
# and if so, appends links to said posts along with topic information to a json file.

import asyncio
from telethon import TelegramClient
from telethon.tl.types import PeerChannel
import json
import re
from collections import defaultdict, OrderedDict




# Replace these with your actual API credentials from my.telegram.org
api_id = xxxxxxx  # Your API ID
api_hash = 'xxxxxxxxxxxxxx'  # Your API Hash
channel_name = "xxxxxxxxxxx"  # Name of the channel


async def test_telethon():
    try:
        async with TelegramClient('test_session', api_id, api_hash) as client:
            
            
            #Here a connection is made with the Medelink channel.
            messages_list = []
            
            me = await client.get_me()  # Fetch your account info
            print(f"Success! Logged in as {me.first_name} (ID: {me.id})")
            dialogs = await client.get_dialogs()  # Fetch all chats
            channel = next((d for d in dialogs if d.name == channel_name), None)
            print(f"Found channel: {channel_name} (ID: {channel.id})")
          
            
            #The last fifty messages in the chanel are examined for Substack posts
            async for message in client.iter_messages(channel, limit=500):
                #Here, we search for Substack posts in the Medelink channel.
                if message.text and re.search(r'https?://[\w.-]*substack\.com[\w/.-]*', message.text):
                    url_match = re.search(r'https?://[\w.-]*substack\.com[\w/.-]*', message.text)
                    url = url_match.group(0) if url_match else None
                    print(message.reply_to_msg_id)
                    
                    #Each post is stored as a json object
                    # 2 corresponds to like, 5 to restack, and 186 to likenote
                    message_data = {
                       "url": url,
                       "like": "FALSE",  # Default values, adjust based on actual message attributes
                       "restack": "FALSE",
                       "likenote": "FALSE"
                       }
                    
                    if message.reply_to_msg_id == 2:
                        message_data['like'] = "TRUE"
                    elif message.reply_to_msg_id == 5:
                        message_data['restack'] = "TRUE"
                    elif message.reply_to_msg_id == 186:
                        message_data['likenote'] == "TRUE"
                    messages_list.append(message_data)


            
            # Dictionary to store merged entries
            merged_messages = defaultdict(lambda: {"like": "FALSE", "restack": "FALSE", "likenote": "FALSE"})
            
            # Process and merge messages
            for message in messages_list:
                url = message["url"]
                merged_messages[url]["url"] = url  # Ensure the URL is set
                for key in ["like", "restack", "likenote"]:
                    if message[key] == "TRUE":
                        merged_messages[url][key] = "TRUE"
            
            # Convert back to a list
            merged_messages_list = [
                    OrderedDict([("url", data["url"]), ("like", data["like"]), ("restack", data["restack"]), ("likenote", data["likenote"])])
                    for data in merged_messages.values()
            ]
            with open('Liker_Data.json', 'w') as json_file:
                json.dump(merged_messages_list, json_file, indent=2)
    except Exception as e:
        print(f"Failed to connect: {e}")



# Run the async function
asyncio.run(test_telethon())
