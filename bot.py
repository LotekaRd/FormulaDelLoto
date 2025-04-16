import asyncio
from telegram.ext import Application, CommandHandler

# Votre token Telegram
TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

# Fonction de démarrage
async def start(update, context):
    await update.message.reply_text("Bonjour ! Je suis votre bot.")

# Fonction principale
async def main():
    # Crée l'application Telegram
    application = Application.builder().token(TOKEN).build()

    # Ajoutez vos handlers ici
    application.add_handler(CommandHandler("start", start))

    # Lancement du bot en polling
    await application.run_polling()

# Lancement du bot
if __name__ == "__main__":
    try:
        asyncio.run(main())  # Essaie d'utiliser asyncio.run
    except RuntimeError as e:
        if str(e) == "This event loop is already running":
            # Si une boucle d'événements existe déjà, utilise une approche différente
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()
        else:
            raise

