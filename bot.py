import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurez le logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Fonction de gestion de la commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf'Bonjour {user.mention_html()}!',
    )

# Fonction de gestion des erreurs
def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

# Fonction principale
async def main() -> None:
    """Start the bot and run polling"""
    # Remplacez 'YOUR_TOKEN' par votre token d'API
    application = Application.builder().token("7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw").build()

    # Ajoutez le gestionnaire de commandes
    application.add_handler(CommandHandler("start", start))

    # Ajoutez le gestionnaire d'erreurs
    application.add_error_handler(error)

    # Exécutez le bot avec un polling
    await application.run_polling()

# Assurez-vous que la boucle d'événements est correctement gérée sans asyncio.run()
if __name__ == '__main__':
    import asyncio
    # Utiliser la boucle d'événements déjà existante
    asyncio.get_event_loop().run_until_complete(main())
