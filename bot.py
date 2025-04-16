import asyncio
from telegram.ext import Application, CommandHandler

# Token Telegram
TELEGRAM_BOT_TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

# Fonction de démarrage
async def start(update, context):
    await update.message.reply_text("Bonjour ! Je suis votre bot.")

# Fonction principale
async def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Ajoutez vos handlers ici
    application.add_handler(CommandHandler("start", start))

    # Démarrez le bot en polling
    await application.run_polling()

# Vérification pour éviter les erreurs de boucle déjà active
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) == "This event loop is already running":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        else:
            raise
