import asyncio
from telegram.ext import Application

TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"  # Votre token Telegram

async def main():
    application = Application.builder().token(TOKEN).build()
    await application.run_polling()

if __name__ == "__main__":
    # Vérifie si une boucle d'événements est déjà en cours
    try:
        # Si aucune boucle d'événements n'est en cours, on utilise asyncio.run()
        asyncio.run(main())
    except RuntimeError:
        # Si une boucle d'événements est déjà en cours, on ne tente pas de la fermer
        print("Une boucle d'événements est déjà en cours.")
