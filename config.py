import os
import platform

username = "" #Facebook email
password = "" #Facebook Password

dir_path = os.path.dirname(os.path.realpath(__file__))


'''
DIRECTORY TO CHROMEDRIVER -- https://chromedriver.storage.googleapis.com/index.html?path=2.39
If you decide to download it make sure to name it the same as in here!
'''
if platform.system() == 'Linux':
	path_of_chrome_driver = dir_path + '/drivers/chromedriver_linux'
elif platform.system() == 'Darwin':
	path_of_chrome_driver = dir_path + '/drivers/chromedriver_mac'
else:
	path_of_chrome_driver = dir_path + '/drivers/chromedriver_windows.exe'


'''
EXTRA.PY TIMINGS 

Time between decisions will only be 1 < n < 3,
so it could wait 1 second or 2 seconds
You can make this faster, but you run the risk of being detected as a bot!
'''
random_time_range_start = 1
random_time_range_end = 3

'''
Messages for matches
Add all the pickup lines you like and the bot will randomly choose which one to send on match!
'''
message_to_send = ["Hey! I heard you are good in algebra, can you replace my X without asking Y? :)",
				   "Do you have a band aid? because I scrape my knee falling for you!",
				   "Hey whats up! :)",
				   "Hey!"]




