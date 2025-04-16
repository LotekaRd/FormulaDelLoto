
import asyncio
from telegram.ext import Application

TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

async def main():
    application = Application.builder().token(TOKEN).build()
    # Ajouter vos gestionnaires ici
    await application.run_polling()

# Utiliser asyncio pour détecter si une boucle existe déjà
try:
    asyncio.get_running_loop()
    # Si une boucle existe déjà, utiliser create_task
    asyncio.create_task(main())
except RuntimeError:
    # Sinon, démarrer une nouvelle boucle
    asyncio.run(main())
