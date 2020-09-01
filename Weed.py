#%%
import os
import time
import shutil
import json
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

ds = open('datesave',) 
date = json.load(ds)

cs = open('cashsave',) 
cash = json.load(cs)

datefin = []

cashfin = []

dat = {

}

rootDir = './'

def toJson(path, name, data):
	filePathName = './' + path + '/' + name
	with open(filePathName, 'w') as fp:
		json.dump(data, fp)

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


def graph():
	lists = sorted(dat.items())
	x, y = zip(*lists)
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
	incoming_int_msg = request.values.get('Body')[1:]
	resp = MessagingResponse()
	msg = resp.message()
	responded = False

##################################################################################
########### CHANGE msg.media TO INCLUDE UPDATED NGROK FORWARDING
##################################################################################

	if 'show' in incoming_msg:
		msg.body("Visualization of Earnings")
		msg.media('http://e4eab3e774d3.ngrok.io/static/chart.png')
		responded = True
		return str(resp)

	if '/' in incoming_msg:
		msg.body("Date Recorded. ")
		date.append(incoming_msg)
		return str(resp)
	
	if 'today' in incoming_msg:
		msg.body("Date Recorded. ")
		date.append(datetime.today().strftime('%m/%d/%y'))
		return str(resp)

	if '$' in incoming_msg:
		msg.body("Amount Recorded. ")
		cash.append(incoming_int_msg)
		return str(resp)
	
	if 'add' in incoming_msg:
		msg.body("Changes Saved! ")
		toJson(rootDir, 'datesave', date)
		toJson(rootDir, 'cashsave', cash)
		conv()
		graph()
		time.sleep(2)
		move()
		return str(resp)


	if 'creator' in incoming_msg:
		msg.body("This Bot was created with love by Adonis Alexis in August of 2020. This Bot is written in python and predominantly utilizes Twilio API and Flask framework to function. For more details, ask the guy showing this to you...")
		responded = True
		return str(resp)

	if 'thank' in incoming_msg:
		msg.body("You're Welcome!")
		responded = True
	
	if 'fuck' in incoming_msg:
		frown = "):"
		msg.body(frown)
		responded = True
	
	if 'reset data' in incoming_msg:
		shutil.copy('saves\cashsave', "cashsave")
		shutil.copy('saves\datesave', "datesave")
		msg.body("Plot data reset!")
		responded = True

	if 'command' in incoming_msg:
		msg.body("COMMAND LIST: \n\n Send dates: \n (Format: mm/dd/yy or use 'today') \n\n Send Amounts: \n (Preface number with $) \n\n Add: \n ('add' Saves date and Amount sent)\n\n Show: \n ('Show' displays Earnings Graph)\n\n Reset Data: \n (COMPLETE RESET) \n\n Remember to say thank you.")
		return str(resp)

	if not responded:
		pa = 'Possible '
		rt = 'Error'
		msg.body(pa + rt)
	


	return str(resp)

if __name__ == '__main__':
	app.run()

 # %%
