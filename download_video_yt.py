import os
import datetime
from telegram import Update
from telegram.ext import ContextTypes
from pytubefix import YouTube

async def download_video_yt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split("/download_video_yt")[1]

    if not url:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='invalid url')
        return

    yt = YouTube(url)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Baixando video: {yt.title}...')

    ys = yt.streams.get_highest_resolution()

    file_name = f'{datetime.datetime.now().timestamp()}.mp4'

    ys.download(output_path="./videos", filename=f'{file_name}')

    path = f'./videos/{file_name}'

    await context.bot.send_video(chat_id=update.effective_chat.id, video=open(f'{path}', "rb"), caption=yt.title)
    os.remove(path)