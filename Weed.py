#%%
import sys
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datefin = []

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
else:
	pass

print(date)
print(cash)
#%%

print(datefin)

plt.plot_date(datefin, cash, marker='o', color='mediumvioletred')
plt.show()

# %%
# Create figure and plot space


# %%
