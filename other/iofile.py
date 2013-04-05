limport numpy as np 
import re

def get_data_from_file(file):
	if file:
		data = np.genfromtxt(file, delimiter=",",dtype= None)
	return np.array([(lambda s: [int(d) for d in s])(re.sub(" +"," ", line).split(' '))  for line in data])

def get_column(data, column, is_sorted=True):
	if is_sorted:
		return np.sort(data[:, column])
