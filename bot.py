import asyncio
from telegram.ext import Application

TOKEN = "7606091350:AAGEKVoR0E-D5rdRQk36LIwdHGlDhlXD4Hw"

async def main():
    application = Application.builder().token(TOKEN).build()

    # Ajoutez ici vos handlers si nécessaire
    # Exemple : application.add_handler(CommandHandler("start", start_handler))

    print("Le bot est en cours d'exécution...")
    await application.run_polling()

if __name__ == "__main__":
    # Cette partie gère le cas où une boucle est déjà en cours d'exécution
    try:
        loop = asyncio.get_event_loop()

        # Si la boucle est déjà en cours, on ne crée pas une nouvelle boucle
        if loop.is_running():
            print("Une boucle d'événements est déjà en cours, lancement dans la boucle existante...")
            loop.create_task(main())  # Ajout de main à la boucle en cours
        else:
            asyncio.run(main())  # Si aucune boucle n'est en cours, on démarre avec asyncio.run()

    except RuntimeError as e:
        if str(e) == "This event loop is already running":
            print("Erreur corrigée : la boucle d'événements est déjà en cours.")
            asyncio.get_event_loop().run_until_complete(main())
        else:
            raise
