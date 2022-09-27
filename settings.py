import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = "5773344026:AAEcTrdqerV8oK3xQX0mY11XeORrVrhjrD0"

TELEGRAM_SUPPORT_CHAT_ID = "-1001862850221"
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)

WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "Поставте Ваше запитання, залиште пропозицію або поскаржтеся 👋")
FEEDBACK_MESSAGE = os.getenv("FEEDBACK_MESSAGE", "Очікуйте 👋")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")