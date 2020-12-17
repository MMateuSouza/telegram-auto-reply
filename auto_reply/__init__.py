import os

from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv(verbose=True)


def auto_reply():
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    session_file = os.getenv('session_file')

    if not api_id or not api_hash or not session_file:
        print('Favor preencher as variáveis no arquivo .env com seus respectivos valores.')
        return

    with TelegramClient(session_file, api_id, api_hash) as client:
        @client.on(events.NewMessage)
        async def _auto_reply(event):
            await event.reply('Infelizmente estou indisponível no momento, por favor tente novamente mais tarde.')

        client.start()
        client.run_until_disconnected()
