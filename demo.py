import os
from flask import Flask, request
import twilio.twiml
from twilio.rest import TwilioRestClient
from random import randint

app = Flask(__name__)

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
client = TwilioRestClient(account_sid, auth_token)

# initialize
callers = []
moderator_number="+15555551212" #your number goes here
twilio_number="+3333333333" #must be a Twilio number from your account
ngrok_url="http://XXX.ngrok.com/" #your ngrok URL

@app.route("/", methods=['GET', 'POST'])
def respond():
	from_number= request.values.get('From')

	if from_number==moderator_number: #moderator number, triggers calls
		connect_callers()
	if from_number not in callers:
		callers.append(from_number)
	print callers
	# respond to incoming text message
	resp = twilio.twiml.Response()
	resp.message("Thanks for playing our game!")
	return str(resp)

def connect_callers():
	pick=randint(0, len(callers)-1)
	number1=callers[pick]
	number2=callers[pick-1]

	client.calls.create(to=number1, from_=twilio_number, url=ngrok_url)
	client.calls.create(to=number2, from_=twilio_number, url=ngrok_url)
	


@app.route("/conference", methods =['GET', 'POST'])
def conference():
	resp = twilio.twiml.Response()
	with resp.dial() as g:
		g.conference("Hackbright")

	return str(resp)


if __name__=="__main__":
	app.run(debug=True)

