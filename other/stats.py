import numpy as np
import re

raw_data = "261 271 236 244 279 296 284 299 288 288 338 360 341 333 261 266 287 296 313 311 299 303 277 283 304 305 288 290 288 289 332 330 309 328 307 328 285 291 295 298 310 318 318 320 333 321 323 324 327 247 256 307 307 297 299 306 315"

data = format_data(raw_data)

LOWEST_VALUE = min(data)
HIGHEST_VALUE = max(data)

class_number = 5

class_width = class_width(HIGHEST_VALUE, LOWEST_VALUE, class_number)

class_limits = get_class_limit(data, class_width)

print class_limits

def class_width(HIGHEST_VALUE, class_number):
	return (HIGHEST_VALUE - LOWEST_VALUE)/class_number

def format_data(data):
	data_array = data.split(' ')
	data_array = [int(data) for data in data_array]

	return np.array(data_array)

print "the class width is {0}".format(class_width)

#frequency table
#class limit
#class boundaries
#frequency
#cumulative frequency
# midpoint
# relative frequency

def get_class_limit(data, width):
	class_limit = []
	first_limit = ()
	temp_value = LOWEST_VALUE
	while limit < HIGHEST_VALUE:
		next_lower_limit = temp_value + width
		class_limit = class_limit.append((temp_value, next_lower_limit-1))
		temp_value = next_lower_limit
    return class_limit

