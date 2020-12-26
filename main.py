from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = 2922002
api_hash = 'b3e3d448e91dccb8e175696a182b28cd'

client = TelegramClient('first', api_id, api_hash)


@client.on(events.NewMessage())
async def handler(event):
    try:
        if event.message.media.document.attributes[0].voice:
            await event.delete()

    except AttributeError:
        pass


client.start()
client.run_until_disconnected()
