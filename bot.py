import logging
from telegram.ext import Application, CommandHandler
import os

# Configurez le niveau de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Remplacez par votre token
TOKEN = '7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw'

async def start(update, context):
    """Envoyer un message lorsque la commande /start est utilisée."""
    await update.message.reply_text('Bonjour! Je suis votre bot.')

def main():
    """Démarre le bot et gère les commandes."""
    application = Application.builder().token(TOKEN).build()

    # Ajoutez le gestionnaire de commande pour la commande /start
    application.add_handler(CommandHandler('start', start))

    # Lancement de la boucle de polling
    application.run_polling()

if __name__ == '__main__':
    main()

