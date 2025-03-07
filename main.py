import threading

import requests


def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()


crypto_response = get_crypto_data()
user_input = input("Enter Your Cryto Currency: ")

x = 0
for crytpo in crypto_response:
    x += 1
    print(x)

    if crytpo["currency"] == user_input:
        print(crytpo["price"])
        break





#"https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"

