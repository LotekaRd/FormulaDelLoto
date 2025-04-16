
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Récupérer le token Telegram depuis les variables d'environnement
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Le token Telegram n'est pas défini ! Ajoutez-le dans les variables d'environnement.")

# Fonction pour répondre à la commande /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bonjour ! Je suis votre bot Telegram prêt à vous aider ! 😊")

# Configurer le bot
def main():
    # Initialiser le bot avec le token
    updater = Updater(token=TOKEN)

    # Ajouter un gestionnaire pour la commande /start
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    # Lancer le bot
    print("Bot en ligne 🚀")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
