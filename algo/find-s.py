# Find-S algo
# example of training set:
# 	variables : Sky - Air Temp - Humidity - Wind - Water - Forecast - EnjoySport

# 	Task: to predict EnjoySport for an arbitrary day

# 	We assume hypothesis h satisfies instance x as positive if h(x) = 1 => EnjoySport = 1


# 	TRAINING_SET = np.array([[1, 1, 1, 1, 1, 1, 1],
# 							[1, 1, 2, 1, 1, 1, 1],
# 							[2, 2, 2, 1, 1, 2, 0],
# 							[1, 1, 2, 1, 2, 2, 1]])
# 	t = find_s(TRAINING_SET)
# 	>> array([1, 1, 0, 1, 0, 0])
# 	Note: 
# 		Data has to be error free 
#  		No real use in real world application
# 		qualitative variables
# 		level of measurement only works for nominal/ordinal

import numpy as np

def find_s(data):
	filtered_traning_set = _ignore_negative(TRAINING_SET)
	hypothesis = filtered_traning_set[0]
	for row in filtered_traning_set:
		if (hypothesis != row).any():
			for i in range(len(row)):
				hypothesis[i] = 0 if hypothesis[i] != row[i] else hypothesis[i]
	return hypothesis 


def _ignore_negative(data):
	temp = [data[:6] for data in TRAINING_SET if data[6] == 1]
	return  np.array(temp)


