import asyncio
from telegram.ext import Application

# Intégration de votre token
TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

async def start_bot():
    application = Application.builder().token(TOKEN).build()
    # Ajouter vos gestionnaires ici
    await application.run_polling()

def main():
    try:
        # Vérifie si une boucle d'événements existe déjà
        asyncio.get_running_loop()
        # Si oui, lance le bot avec `create_task`
        asyncio.create_task(start_bot())
    except RuntimeError:
        # Si aucune boucle n'existe, utilise `asyncio.run`
        asyncio.run(start_bot())

if __name__ == "__main__":
    main()
