import asyncio
from telegram.ext import Application

# Votre token Telegram
TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

async def start_bot():
    # Crée une instance de l'application Telegram
    application = Application.builder().token(TOKEN).build()
    # Ajoutez ici vos gestionnaires (handlers) si nécessaire
    print("Le bot est en cours d'exécution...")
    await application.run_polling()

def main():
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Si une boucle existe déjà, planifiez la tâche avec `create_task`
            asyncio.create_task(start_bot())
        else:
            # Sinon, lancez le bot avec `asyncio.run`
            asyncio.run(start_bot())
    except RuntimeError:
        # Si aucune boucle n'est disponible, créez-en une nouvelle
        asyncio.run(start_bot())

if __name__ == "__main__":
    main()
