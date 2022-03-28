import os
from dotenv import load_dotenv

load_dotenv()

# Obtener el api del bot desde un archivo .env
BOT_TOKEN = os.getenv('BOT_TOKEN')
