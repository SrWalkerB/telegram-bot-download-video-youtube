import os
from telegram import Update
from telegram.ext import ContextTypes
from pytubefix import YouTube
from youtube_util import YoutubeUtilService

async def download_video_yt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split("/download_video_yt")[1]

    if not url:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='invalid url')
        return

    yt = YoutubeUtilService(url)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Baixando video: {yt.getTitle()}...')

    yt.download_video()

    await context.bot.send_video(chat_id=update.effective_chat.id, video=open(f'{yt.get_path_video()}', "rb"), caption=yt.getTitle())
    os.remove(yt.get_path_video())