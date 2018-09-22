from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import random
import time
import os
import platform
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))

if platform.system() == 'Linux':
    path_of_chrome_driver = dir_path + '/drivers/chromedriver_linux'
elif platform.system() == 'Darwin':
    path_of_chrome_driver = dir_path + '/drivers/chromedriver_mac'
else:
    path_of_chrome_driver = dir_path + '/drivers/chromedriver_windows.exe'

date_time_log = time.strftime('%d/%m/%Y %H:%M:%S')
chrome_settings = Options()

random_time_range_start = 1
random_time_range_end = 3

message_to_send = ["Hey! I heard you are good in algebra, can you replace my X without asking Y? :)",
                   "Do you have a band aid? because I scrape my knee falling for you!",
                   "Hey whats up! :)",
                   "Hey!"]

class Randomizer:
	def decision(self):
		x = random.randint(0,1)
		return x

	def random_time(self):
		x = random.randint(random_time_range_start,random_time_range_end)
		return x

	def random_pickup_line(self):
		amount_of_pickup_lines = len(message_to_send)
		amount_of_pickup_lines -= 1
		x = random.randint(0,amount_of_pickup_lines)
		return x


class TinderBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome(path_of_chrome_driver, chrome_options=chrome_settings)
		self.randomizer = Randomizer()

	def log(self,message):
		logging.basicConfig(filename='autoswiper.log',level=logging.DEBUG)
		logging.debug((message.upper()) + ' ' + date_time_log)
		print(message)

	def open_tinder(self):
		self.log('***** from openTinder() START *****')
		try:
			self.driver.get("https://tinder.com/app/login")
			time.sleep(7)
			self.driver.implicitly_wait(60)
			log_in = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button')
			log_in.click()
		except NoSuchElementException as e:
			self.log('***** ERROR: ' + str(e))
			self.log('***** from openTinder() END *****')
		self.driver.switch_to_window(self.driver.window_handles[-1])

	def fb_login(self):
		self.log('***** from fbLogin() START *****')
		self.driver.implicitly_wait(20)
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.username)
		self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(self.password)
		self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
		self.driver.switch_to_window(self.driver.window_handles[0])
		self.log('***** Logged in!')
		self.log('***** from fbLogin() END *****')

	def skip_intro(self):
		self.log('***** skip_intro START *****')
		try:
			self.driver.implicitly_wait(10)
			time.sleep(2)
			next_1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div[1]/div[1]/div/div[3]/button")
			next_1.click()

			self.driver.implicitly_wait(10)
			time.sleep(2)
			next_2 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div/main/div/div[3]/button")
			next_2.click()

			self.driver.implicitly_wait(10)
			time.sleep(2)
			location_3 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div/div[3]/button[1]")
			location_3.click()

			self.driver.implicitly_wait(10)
			time.sleep(2)
			no_notifications_4 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div/div[3]/button[2]")
			no_notifications_4.click()
		except NoSuchElementException as e:
			self.log('***** ERROR: ' + str(e))
			self.log('Skipping clicks!')
		self.log('***** skip_intro END *****')

	def check_if_matched(self):
		self.log('***** check_if_matched START *****')
		matched = False
		time_between = self.randomizer.random_time()
		try:
			self.driver.implicitly_wait(5)
			send_message_to_match = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/a")
			keep_swiping = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/button")
			self.log('****** Found Match!')

			if send_message_to_match:
				matched = True

		except NoSuchElementException as e:
			self.log('***** ERROR: ' + str(e))
			self.log('***** No Matches! :(\n')

		if matched == True:
			send_message_to_match.click()
			self.log('***** Im inside the match chat!')

			time.sleep(time_between)

			chat_box = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/textarea")
			random_val = self.randomizer.random_pickup_line()
			line = message_to_send

			chat_box.send_keys(line[random_val])
			self.log('***** Wrote Message on chat_box')

			time.sleep(time_between)

			send_button = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/button")
			send_button.click()
			self.log(time_between)

			time.sleep(time_between)

			exit = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/nav/a/div")
			exit.click()
			self.log('***** I have exited the match! and messaged succesfully')
			self.log('***** Will keep swiping!')
		else:
			self.log('***** No matches *****')
		self.log('***** check_if_matched END *****')

	def like(self):
		while True:
			self.log('***** like() Main function within script START ')
			try:
				self.driver.implicitly_wait(60)
				like = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[4]/span")
				dislike = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[2]/span")
				time_between = self.randomizer.random_time()
				self.log('***** like() The time to wait is: ' + str(time_between))
				time.sleep(time_between)
				decision = self.randomizer.decision()
				self.log('***** Took decision: ' + str(decision))
				if decision == 1:
					like.click()
					self.log('***** Liked! with decision: ' + str(decision) + ' and time in between: ' + str(time_between))
					self.check_if_matched()
				else:
					dislike.click()
					self.log('***** Disliked! with decision: ' + str(decision) + ' and time in between: ' + str(time_between))
			except NoSuchElementException as e:
				self.log('***** ERROR: ' + str(e))
			self.log('***** like() Main function within script END *****')

	def start(self):
		try:
			self.open_tinder()
			self.fb_login()
			self.skip_intro()
			self.check_if_matched()
			self.like()
			self.driver.quit()
		except Exception as error:
			self.log('***** ERROR FROM start() *****')
			self.log(str(error))












		
