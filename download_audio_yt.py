import os

from telegram import Update
from telegram.ext import ContextTypes
from youtube_util import YoutubeUtilService
from models.userCommandRequestModel import UserCommandRequestModel

async def download_audio_yt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.split('/download_audio_yt')[1]

    if not url:
        await  context.bot.send_message(chat_id=update.effective_chat.id, text='Invalid URL')
        return
    
    yt = YoutubeUtilService(url)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Baixando audio: {yt.getTitle()}...')

    yt.download_audio()
    userCommandRequestModel = UserCommandRequestModel()

    await context.bot.send_audio(chat_id=update.effective_chat.id, caption=f'{yt.getTitle()}', audio=open(f'{yt.get_path_audio()}', "rb"))

    userCommandRequestModel.insert({
        "chat_id": update.effective_chat.id,
        "user_full_name": update.effective_chat.full_name,
        "command_used": "/download_audio_yt",
        "youtube_response": {
            "url": url.strip(),
            "title": yt.getTitle()
        }
    })

    os.remove(yt.get_path_audio())
