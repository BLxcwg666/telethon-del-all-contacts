from telethon.sync import TelegramClient
from telethon import functions
from telethon.errors.rpcerrorlist import FloodWaitError
import time

api_id = 'your_api'
api_hash = 'your_hash'

client = TelegramClient('account', api_id, api_hash)

with client:
    contacts = client(functions.contacts.GetContactsRequest(
        hash=0
    ))

    contact_ids = [contact.user_id for contact in contacts.contacts]

    for contact_id in contact_ids:
        try:
            result = client(functions.contacts.DeleteContactsRequest(
                id=[contact_id]
            ))
            print(f"Deleted ID: {contact_id}")
        except FloodWaitError as e:
            print(f"FloodWaitError: Waiting for {e.seconds} seconds.")
            time.sleep(e.seconds + 1)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            time.sleep(0.5)
