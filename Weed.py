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

date = []
cash = []
datefin = []
cashfin = []

def numberer(x): 
	for i in x:
		cashfin.append(int(i))

def dater(x):
	for dt in x:
		datefin.append(datetime.strptime(dt, '%m/%d/%y'))


def wcalc():

	year = input("What Year Is It? (YYYY)")

	fir = input("First date out of 5: MM/DD")
	fir = fir + "/" + year[-2:]
	firc = input("Amount Made: ")

	sec = input("Second date out of 5: MM/DD")
	sec = sec + "/" + year[-2:]
	secc = input("Amount Made: ")

	thi = input("Third date out of 5: MM/DD")
	thi = thi + "/" + year[-2:]
	thic = input("Amount Made: ")

	fou = input("Fourth date out of 5: MM/DD")
	fou = fou + "/" + year[-2:]
	fouc = input("Amount Made: ")

	fif = input("Fifth date out of 5: MM/DD")
	fif = fif + "/" + year[-2:]
	fifc = input("Amount Made: ")

	date.extend([fir, sec, thi, fou, fif])
	cash.extend([firc, secc, thic, fouc, fifc])

def test():
	fir = '7/17/20'
	firc = '90'
	sec = '7/19/20'
	secc = '107'
	thi = '7/28/20'
	thic = '126'
	fou = '8/3/20'
	fouc = '100'
	fif = '8/6/20'
	fifc = '169'

	date.extend([fir, sec, thi, fou, fif])
	cash.extend([firc, secc, thic, fouc, fifc])


def graph():
	plt.figure(figsize=(15,15))
	plt.plot_date(datefin, cashfin, marker='o', linestyle = '-', color='mediumvioletred')
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
		dater(date)
		numberer(cash)
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
