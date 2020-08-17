#%%
from twilio.rest import Client
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

account_sid = 'ACdf779c87eb69f16a893c436695c4779f'
auth_token = '7301f66dcd1ed9db550f1e1434fa2274'
client = Client(account_sid, auth_token)

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

#%%
ini = input("Welcome to 'Weed'Calculator! /n Type 1 To Begin: ")

date = []
cash = []




if ini == "1":
	wcalc()
	dater(date)
	numberer(cash)
else:
	pass

print(date)
print(cash)
#%%

print(datefin)
print(cashfin)

plt.figure(figsize=(15,15))
plt.plot_date(datefin, cashfin, marker='o', linestyle = '-', color='mediumvioletred')
plt.show()



# %%
message = client.messages \
    .create(
         body='I love Makayla',
         from_='+19362182353',
         to='+17277440419'
     )

print(message.sid)

# %%
