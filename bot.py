from telegram.ext import Application, CommandHandler

# Votre token Telegram
TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

# Fonction de démarrage
async def start(update, context):
    await update.message.reply_text("Bonjour ! Je suis votre bot.")

# Fonction principale
def main():
    # Crée l'application Telegram
    application = Application.builder().token(TOKEN).build()

    # Ajoutez vos handlers ici
    application.add_handler(CommandHandler("start", start))

    # Lancement en utilisant la méthode asynchrone proprement
    application.run_polling()

if __name__ == "__main__":
    main()

