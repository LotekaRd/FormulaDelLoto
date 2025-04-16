import asyncio
from telegram.ext import Application, CommandHandler

# Remplacez "votre_token" par votre token Telegram
TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

async def start(update, context):
    await update.message.reply_text("Bonjour! Je suis votre bot.")

async def main():
    application = Application.builder().token(TOKEN).build()

    # Ajoutez des gestionnaires
    application.add_handler(CommandHandler("start", start))

    # Exécutez le bot
    await application.run_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(main())
    else:
        asyncio.run(main())
