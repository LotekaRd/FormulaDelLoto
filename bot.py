from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Fonction de commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bonjour, je suis votre bot!")

# Fonction principale pour démarrer le bot
async def main():
    application = Application.builder().token('7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw').build()

    # Ajout de la commande /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Lancement du bot et gestion des mises à jour en continu
    await application.run_polling()

if __name__ == "__main__":
    # Exécution du bot sans utiliser asyncio.run
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
