
import numpy as np
import re
import math

def class_width(HIGHEST_VALUE, class_number):
	return (HIGHEST_VALUE - LOWEST_VALUE)/class_number

def format_data(data):
	data_array = data.split(' ')
	data_array = [int(data) for data in data_array]

	return np.array(data_array)

def get_class_limit(data, width):
	class_limit = []
	first_limit = ()
	temp_value = LOWEST_VALUE
	while limit < HIGHEST_VALUE:
		next_lower_limit = temp_value + width
		class_limit = class_limit.append((temp_value, next_lower_limit-1))
		temp_value = next_lower_limit
  	return class_limit

def mode(data):
	"""
	Evaluate the mode, the value that occurs the most frequently

	Return a tuple ((maximu number, index number), data)
	>>> data = [1,4,3,3,5,5,6,1,1,7,7,5,5,7,7,7,7,7,7,7,9,9,0]
	>>> print mode(data)
	"""
	data = sorted(data)
	maxim = 0
	max_temp = (0, 0)
	num_max = data[0]
	for i in range(len(data)):
		if num_max == data[i]:
			maxim += 1
			if i == len(data)-1 and max_temp[0]<maxim:
				return (maxim, data[i]), data		
		elif max_temp[0] < maxim:
			max_temp = (maxim, data[i-1])
			num_max = data[i]
			maxim = 1
		else:
			num_max = data[i]
			maxim = 1

	return max_temp, data	

def median(data):
	"""
		evaluate the median of a sequence of data
		
		>>> data = [12, 12, 13, 13, 15, 15,
				17, 17, 12, 12, 12, 12, 
				12, 13, 13, 14, 14, 14, 
				15, 15, 16, 16, 16, 17,
				18, 18, 18, 19, 12, 14,
				16, 19, 12, 12, 15, 15, 
				17, 17, 20, 20]
		>>> print median(data)
	"""	
	data = sorted(data)
	length = len(data)
	position = (length + 1) / 2
	if length % 2 == 0 :
		return (data[position-1] + data[position]) / float(2), data
	else: 
		return data[position-1], data


def mean(data,):
	return sum(data) / float(len(data))
	
def variance(data, type="sample"):
	if type != "sample":
		return sum(map(lambda x: (x - mean(data)) ** 2, data)) / float( len(data) )
	return sum(map(lambda x: (x - mean(data)) ** 2, data)) / float( len(data) -1 )

def std_deviation(data, type="sample"):
	if type != "sample":
		return math.sqrt(variance(data, type="population"))
	return math.sqrt(variance(data))

#print mean()

# raw_data = "261 271 236 244 279 296 284 299 288 288 338 360 341 333 261 266 287 296 313 311 299 303 277 283 304 305 288 290 288 289 332 330 309 328 307 328 285 291 295 298 310 318 318 320 333 321 323 324 327 247 256 307 307 297 299 306 315"

# data = format_data(raw_data)

# LOWEST_VALUE = min(data)
# HIGHEST_VALUE = max(data)

# class_number = 5

# class_width = class_width(HIGHEST_VALUE, class_number)

# class_limits = get_class_limit(data, class_width)

# print class_limits

# print "the class width is {0}".format(class_width)
