
import numpy as np
import re
import math
from collections import OrderedDict

def class_width(data, class_number):
	return ((max(data) - min(data))/class_number) + 1

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

#********** Central Tendency ************

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
	return data[position-1], data


def mean(data,):
	return sum(data) / float(len(data))
	
def variance(data, type="sample"):
	sum_of_squares = sum(map(lambda x: (x - mean(data)) ** 2, data))
	if type != "sample":
		return sum_of_squares / float( len(data) )
	return sum_of_squares / float( len(data) -1 )

def std_deviation(data, type="sample"):
	if type != "sample":
		return math.sqrt(variance(data, type="population"))
	return math.sqrt(variance(data))

def stem_and_leaf(data, size_stem=1):
	"""
	Construct a stem and leaf display
	@var data string 
	@var size_stem int : number of digit

	>>> data = [12, 12, 13, 13, 15, 15,
				17, 17, 12, 12, 12, 12, 
				12, 13, 13, 14, 14, 14, 
				15, 15, 16, 16, 16, 17,
				18, 18, 18, 19, 12, 14,
				16, 19, 12, 12, 15, 15, 
				17, 17, 20, 20]
	>>>  stem_and_leaf(data)

	1 | 2 2 3 3 5 5 
	2 | 0 0 
	"""
	data = sorted(data)
	display = OrderedDict()
	min_digit_size = size_stem + 1
	for item in data:
		str_item = str(item)
		if len(str_item) < min_digit_size:
			str_item = '0%s' % str_item

		if str_item[0] not in display:
			display[str_item[0]] = [str_item[1:]]
		else:
			display[str_item[0]].append(str_item[1:])

	#display stem and leaf 
	for k , v in display.iteritems():
		print "{0} | {1}".format(k, ' '.join(v))

def coefficient_of_variance(data):
	return (std_deviation(data) / float(mean(data))) * 100

#*********** Probability *************

def factorial(n):
	#dependent
	#using Y combinator
	return (lambda f: (lambda c: c(c))(lambda x: f(lambda t: x(x)(t))))(lambda c: lambda n: 1 if n<=1 else n*c(n-1))(n)

def permutation(n, c):
	#grouping with order
	return factorial(n) / float(factorial(n - c))

def combination(n, c):
	#grouping
	return factorial(n) / float(factorial(n)) * factorial(n-c)



# def fact(n):
# 	if n <= 1:
# 		return 1
# 	return n * factorial(n-1)
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
