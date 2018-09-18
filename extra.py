import random
import config

'''
Binary decision making. Like = 1 and Dislike = 0
'''
def decision():
	x = random.randint(0,1)
	return x

'''
Randomizes time between likes or dislikes in seconds
'''
def random_time():
	x = random.randint(config.random_time_range_start,config.random_time_range_end)
	return x 

'''
Randomizes pickupline chosen to be sent
'''
def random_pickup_line():
	amount_of_pickup_lines = len(config.message_to_send)
	x = random.randint(0,amount_of_pickup_lines)
	return x
