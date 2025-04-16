
import asyncio
from telegram.ext import Application

TOKEN = " 7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw "

async def main():
    application = Application.builder().token(TOKEN).build()
    # Ajouter vos gestionnaires ici
    await application.run_polling()

# Si une boucle d'événements est déjà en cours, utilisez asyncio.get_event_loop()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

