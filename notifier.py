import requests

def send_telegram_alert(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=payload, timeout=10)

        if response.status_code == 200:
            print("Telegram alert sent successfully.")
        else:
            print("Failed to send alert:", response.text)

    except requests.exceptions.RequestException as e:
        print("Telegram connection error:", e)