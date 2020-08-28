#%%
import os
import shutil
import pickle
from flask import Flask, request
from flask import render_template
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio.rest import Client
import sys

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

account_sid = 'ACdf779c87eb69f16a893c436695c4779f'
auth_token = '7301f66dcd1ed9db550f1e1434fa2274'
client = Client(account_sid, auth_token)


date = ['7/17/20', '7/19/20', '7/28/20', '8/3/20', '8/6/20']

cash = ['90', '107', '126', '100', '169']

datefin = []

cashfin = []

dat = {

}

def conv():
	i = 0
	j = 0			
							
	while i <= (len(date) - 1):	
				
		datefin.append(datetime.strptime(date[j], '%m/%d/%y'))
		
		cashfin.append(int(cash[j]))
		
		dat.update( {datefin[j] : cashfin[j]} )
		
		j += 1
		i += 1
		print (i)


	lists = sorted(dat.items())
	x, y = zip(*lists)


def graph():
	plt.figure(figsize=(15,10))
	plt.plot_date(x, y, marker='o', linestyle = '-', color='mediumvioletred')
	plt.savefig('chart.png')

def move():
	shutil.move('chart.png', "static\chart.png")


@app.route("/", methods=['GET'])
def hello():
	return(render_template('index.html'))

@app.route('/sms', methods=['POST'])
def sms():
	incoming_msg = request.values.get('Body').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False

##################################################################################
########### CHANGE msg.media TO INCLUDE UPDATED NGROK FORWARDING
##################################################################################

	if 'show' in incoming_msg:
		msg.body("Available")
		msg.media('http://7c79dbe462fd.ngrok.io/static/chart.png')
		responded = True
		return str(resp)

	if '/' in incoming_msg:
		msg.body("Date Recorded. ")
		date.append(incoming_msg)
		return str(resp)

	if '190' in incoming_msg:
		msg.body("Amount Recorded. ")
		cash.append(incoming_msg)
		return str(resp)
	
	if 'add' in incoming_msg:
		msg.body("All set!")
		conv()
		graph()
		return str(resp)

	if 'push' in incoming_msg:
		msg.body("Changes Saved! ")
		move()
		return str(resp)


	if not responded:
		pa = 'Not '
		rt = 'Available'
		msg.body(pa + rt)
	
	return str(resp)


if __name__ == '__main__':
	app.run()



#%%
ini = input("Welcome to 'Weed' Calculator! | Type 1 To Begin: ")

if ini == "1":
	wcalc()
	dater(date)
	numberer(cash)
elif ini.upper() == "TEST":
	test()
	dater(date)
	numberer(cash)
else:
	pass

print(date)
print(cash)
#%%

print(datefin)
print(cashfin)

plt.figure(figsize=(10,10))
plt.plot_date(datefin, cashfin, marker='o', linestyle = '-', color='mediumvioletred')
plt.savefig('chart.png')



   # %%
print(date)
print(cash)
# %%
