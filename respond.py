from flask import Flask
from twilio import twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def respond():
	#Respond to incoming text message with a static response
	resp = twiml.Response()
	resp.message("Hello from the Hackbright Academy")

	return str(resp)

if __name__=="__main__":
	app.run(debug=True)