from telegram import Update
from telegram.ext import Application, CommandHandler

# Remplacez ceci par votre token
TOKEN = " 7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw "

# Fonction pour démarrer le bot
async def start(update: Update, context):
    await update.message.reply("Bonjour, je suis votre bot!")

# Fonction principale pour lancer l'application
async def main():
    # Créez l'application et passez le token
    application = Application.builder().token(TOKEN).build()

    # Ajoutez un gestionnaire de commande "/start"
    application.add_handler(CommandHandler("start", start))

    # Démarrer le bot
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
