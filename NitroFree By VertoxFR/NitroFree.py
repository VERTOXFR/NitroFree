import requests
import json
import time
import random
import string

# ---
# Coded by VertoxFR
# Github: https://github.com/VERTOXFR/NitroFree.git
# ---

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

if __name__ == "__main__":
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }

    data = {
        'partnerUserId': generate_random_string(64)
    }

    session = requests.Session()

    try:
        while True:
            response = session.post(url, headers=headers, json=data)

            if response.status_code == 200:
                token = response.json()['token']
                with open('codes.txt', 'a') as file:
                    file.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n")
                print("Ton nitro a etait sauvegarder dans codes.txt.")
            elif response.status_code == 429:
                print("Relancer le programme.")
                time.sleep(60)
            elif response.status_code == 504:
                print("relancer dans 5 seconde.")
                time.sleep(5)
            else:
                print(f"Request failed with status code {response.status_code}.")
                print(f"Error message: {response.text}")

            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        session.close()
