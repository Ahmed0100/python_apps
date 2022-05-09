import requests
import time

api_key= '3bf7ddaf-4088-4bef-8466-d8a0a0c4e52d'
bot_key = '1945211857:AAH2HF8R_O29oYjZTHNoAAR-m42jbYSuav0'
chat_id = '1676975619'

limit = 25000
time_interval = 5

def get_price():
	url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
	parameters = {
		'start':'1',
		'limit':'2',
		'convert':'USD'
	}
	headers = {
		'Accepts': 'application/json',
		'X-CMC_PRO_API_KEY': api_key,
	}
	response = requests.get(url,headers=headers, params=parameters).json()
	btc_price=response['data'][0]['quote']['USD']['price']

	return btc_price

def send_update(chat_id, msg):
	url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
	requests.get(url)

def main():
	while True:
		price= get_price()
		print(price)
		if price < limit:
			send_update(chat_id, f"Hi se3r el btc b2a kda : {price}")

		time.sleep(time_interval)

main()