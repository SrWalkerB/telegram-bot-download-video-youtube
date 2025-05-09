import os
import datetime

from telegram import Update
from telegram.ext import ContextTypes
from pytubefix import YouTube

async def download_audio_yt(update: Update, content: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split('/download_audio_yt')[1]

    if not url:
        await  content.bot.send_message(chat_id=update.effective_chat.id, text='Invalid URL')
        return
    
    yt = YouTube(url)

    ys = yt.streams.get_audio_only()

    file_name = f'{datetime.datetime.now().timestamp()}.mp4'

    ys.download(output_path="./audio", filename=file_name)

    path = f'./audio/{file_name}'

    print(file_name)

    await content.bot.send_audio(chat_id=update.effective_chat.id, caption=f'{ys.title}', audio=open(f'{path}', "rb"))
    os.remove(path)
