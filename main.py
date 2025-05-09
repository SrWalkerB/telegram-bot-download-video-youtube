import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv

from download_video_yt import download_video_yt
from download_audio_yt import download_audio_yt

load_dotenv(".env")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def dog_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dog_response = requests.get("https://random.dog/woof.json")

    await context.bot.send_photo(chat_id=update.effective_chat.id, caption="🐶", photo=dog_response.json()["url"])

print("Start Bot")

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

dog_handler = CommandHandler("dog", dog_command)
download_video_yt_handler = CommandHandler("download_video_yt", download_video_yt)
download_audio_yt_handler = CommandHandler("download_audio_yt", download_audio_yt)

application.add_handler(dog_handler)
application.add_handler(download_video_yt_handler)
application.add_handler(download_audio_yt_handler)

application.run_polling()