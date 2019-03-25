import requests
import configurations

def point(event, context):
	print(event)
	
	message_text = event["message"]["text"]
	chat_id = event["message"]["chat"]["id"]

	text = "Бот готов"
	send_message(chat_id, text)

def send_message(chat_id, text):
	url = "https://api.telegram.org/bot{token}/{method}".format(
		token = configurations.token,
		method = "sendMessage"
	)
	data = {
		"chat_id": chat_id,
		"text": text
	}
	r = requests.post(url, data = data)
	print(r.json())