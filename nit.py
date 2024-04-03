import requests
import random
import string
import time

discord_webhook_url = "https://discord.com/api/webhooks/1210349485172199424/MGml5bHCoM3exBNgT3-_9DOTPkQ6wOeqSYIXaQn3vgEIvPD9cK65SGkd-JcdDh78-8VI"

def generate_random_string(length=18):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_request_and_check_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord_webhook(code)
        
def send_to_discord_webhook(code):
    data = {"content": f"@here Found a valid code by hassen : {code}"}
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code != 200:
        print("Failed to send message to Discord webhook")

if __name__ == "__main__":
    while True:
        code = generate_random_string()
        send_request_and_check_code(code)
        time.sleep(1)