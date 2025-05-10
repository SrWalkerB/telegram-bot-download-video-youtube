import os

from telegram import Update
from telegram.ext import ContextTypes
from youtube_util import YoutubeUtilService

async def download_audio_yt(update: Update, content: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split('/download_audio_yt')[1]

    if not url:
        await  content.bot.send_message(chat_id=update.effective_chat.id, text='Invalid URL')
        return
    
    yt = YoutubeUtilService(url)

    yt.download_audio()

    await content.bot.send_audio(chat_id=update.effective_chat.id, caption=f'{yt.getTitle()}', audio=open(f'{yt.get_path_audio()}', "rb"))
    os.remove(yt.get_path_audio())
