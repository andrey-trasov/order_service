import requests

from service.settings import TELEGRAM_TOKEN

def sending_telegram_message(tg_id):
    if tg_id:
        params = {
          "text": f"Вам пришёл новый заказ!",
          "chat_id": str(tg_id),
        }
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=params)