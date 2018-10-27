from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

N = 100 #number of square divisions of our area

def parser(x):
	return datetime.strptime('19'+x, '%Y-%b')

pressure_field = [[0 for i in range(N)] for j in range(N)] #area in which we have to predict

# for (i,j) block our data will be in file pdataij.csv i.e. for (2,1) file is pdata21.csv

# pressure prediction

for i in range(N):
	for j in range(N):
		name = 'pdata'+str(i)+str(j)+'.csv'
		data = read_csv(name, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
		x = data.values
		size = int(len(X) * 0.80)
		train, test = x[0:size],x[size:len(x)]
		history = [x for x in train]
		predictions = []
		for t in range(len(test)):
			model = ARIMA(history, order=(2,1,1))
			fit = model.fit(disp = 0)
			output = fit.forecast()
			predictions.append(output[0])
			history.append(test[t])

		model = ARIMA(history, order=(2,1,1))
		fit = model.fit(disp = 0)
		output = fit.forecast()
		pressure_field[i][j] = output[0]


#predict the wind: x-axis
u_field = [[0 for i in range(N)] for j in range(N)] #area in which we have to predict

# for (i,j) block our data will be in file udataij.csv i.e. for (2,1) file is udata21.csv

# x-axis wind velocity prediction

for i in range(N):
	for j in range(N):
		name = 'udata'+str(i)+str(j)+'.csv'
		data = read_csv(name, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
		x = data.values
		size = int(len(X) * 0.80)
		train, test = x[0:size],x[size:len(x)]
		history = [x for x in train]
		predictions = []
		for t in range(len(test)):
			model = ARIMA(history, order=(2,1,1))
			fit = model.fit(disp = 0)
			output = fit.forecast()
			predictions.append(output[0])
			history.append(test[t])

		model = ARIMA(history, order=(2,1,1))
		fit = model.fit(disp = 0)
		output = fit.forecast()
		u_field[i][j] = output[0]


#predict the wind: y-axis
v_field = [[0 for i in range(N)] for j in range(N)] #area in which we have to predict

# for (i,j) block our data will be in file vdataij.csv i.e. for (2,1) file is vdata21.csv

# y-axis wind velocity prediction

for i in range(N):
	for j in range(N):
		name = 'vdata'+str(i)+str(j)+'.csv'
		data = read_csv(name, header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
		x = data.values
		size = int(len(X) * 0.80)
		train, test = x[0:size],x[size:len(x)]
		history = [x for x in train]
		predictions = []
		for t in range(len(test)):
			model = ARIMA(history, order=(2,1,1))
			fit = model.fit(disp = 0)
			output = fit.forecast()
			predictions.append(output[0])
			history.append(test[t])

		model = ARIMA(history, order=(2,1,1))
		fit = model.fit(disp = 0)
		output = fit.forecast()
		v_field[i][j] = output[0]


# Now we have wind direction plots in vector form and pressure data over desired location. In case of any cyclone we will get a wind vector loop.

# Now take reverse curl of the vectors obtained and detect the loops in near future for any cyclone.