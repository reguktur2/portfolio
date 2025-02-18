from mailjet_rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
def sendMesage(Subject, text='', additional=''):
	message = {
	'Messages': [
					{
						"From": {
								"Email": "schookg7@gmail.com",
								"Name": "Me"
						},
						"To": [
								{
								"Email": "nazarkomarnik@gmail.com",
								"Name": "You"
								}
						],
						"Subject": Subject,
						"TextPart": text,
						"HTMLPart": additional
					}
			]
	}
	return message

# message = sendMesage('Тест повідомлення', 'Перевірка успішна✅', '<h1>Checkpoint</h1>')

# result = mailjet.send.create(data=message)
# print (result.json())