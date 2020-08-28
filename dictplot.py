import matplotlib.pyplot as plt
from datetime import datetime

date = ['7/17/20', '7/19/20', '7/28/20', '8/3/20', '8/6/20']

cash = ['90', '107', '126', '100', '169']

datefin = []

cashfin = []

dat = {

}

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

			
plt.figure(figsize=(15,10))
plt.plot_date(x, y, marker='o', linestyle = '-', color='mediumvioletred')
plt.show()


