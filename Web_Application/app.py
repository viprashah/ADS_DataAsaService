
# coding: utf-8

# In[ ]:

from flask import Flask, jsonify,render_template, request

import logging,numbers, sys, threading
from satori.rtm.client import make_client, SubscriptionMode

app = Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/send', methods = ['GET','POST'])
def get_prev_close_price():
			stock = request.form['stock']
			print(stock)
			data = call_stock_data(stock)
			prev_close_price = data.get_prev_close()
			yhigh =  data.get_year_high()
			ylow =  data.get_year_low()
			result = type(prev_close_price)
			print(result)
			if result:return render_template('index.html' , pcp = prev_close_price , yh = yhigh , yl =ylow )
			else: return render_template('index.html' , pcp ="No value")
			


def call_stock_data(stock):
        # Get stock data

        from yahoo_finance import Share
        stock = Share(stock)
        return stock
		
		
channel = "youtube"
endpoint = "wss://open-data.api.satori.com"
appkey = "AbCA2E913c6cFeE6C193DC6e7d80dFc3"


def main():
    with make_client(
            endpoint=endpoint, appkey=appkey) as client:

        print('Connected!')

        mailbox = []
        got_message_event = threading.Event()

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    mailbox.append(message)
                got_message_event.set()

        subscription_observer = SubscriptionObserver()
        client.subscribe(
            channel,
            SubscriptionMode.SIMPLE,
            subscription_observer)


        if not got_message_event.wait(10):
            print("Timeout while waiting for a message")
            sys.exit(1)

        for message in mailbox:
            print('Got message "{0}"'.format(message))
	


if __name__ == '__main__':
	main()
app.run(debug=True)
			




