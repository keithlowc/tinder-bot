#!/usr/bin/env python 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time
import logging
import extra
import config

date_time_log = time.strftime('%d/%m/%Y %H:%M:%S')
chrome_settings = Options()
#chrome_settings.add_argument('--headless') - Headless mode still in development
#chrome_settings.add_argument('--window-size=1920x1080') - Headless mode still in development

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(config.path_of_chrome_driver, options=options, chrome_options=chrome_settings)

def log(message):
    logging.basicConfig(filename='autoswiper.log',level=logging.DEBUG)
    logging.debug((message.upper()) + ' ' + date_time_log)
    print(message)
    
'''
(STEP 1)
Opens tinder website
'''
def openTinder():
    log('***** from openTinder() START *****')
    try:
        driver.get("https://tinder.com/app/login")
        time.sleep(7)
        driver.implicitly_wait(60)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/button').click()
        log('***** Opening Tinder!')
    except NoSuchElementException as e:
        log('ERROR: ' + e)
    log('***** from openTinder() END *****')

print (time.strftime('%d/%m/%Y %H:%M:%S'))
    
'''
(STEP 2)
Sends your information into the facebook form, and logs you in
'''
def fbLogin():
    log('***** from fbLogin() START *****')
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(config.username) 
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(config.password)
    driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
    log('***** Logged in!')
    log('***** from fbLogin() END *****')

'''
(STEP 3)
Clicks the new intro tinder website has
'''
def skip_intro():
    log('***** skip_intro START ****')
    try:
        driver.implicitly_wait(10)
        time.sleep(2)
        next_1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div[1]/div[1]/div/div[3]/button")
        next_1.click()
        
        driver.implicitly_wait(10)
        time.sleep(2)
        next_2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div/main/div/div[3]/button")
        next_2.click()

        driver.implicitly_wait(10)
        time.sleep(2)
        location_3 = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div/div[3]/button[1]")
        location_3.click()

        driver.implicitly_wait(10)
        time.sleep(2)
        no_notifications_4 = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[2]/div/div/div[1]/div/div[3]/button[2]")
        no_notifications_4.click()
    except NoSuchElementException as e:
        log('ERROR: ' + e)
        log('Skipping clicks!')
    log('***** skip_intro END ****')

'''
(STEP 4 only if matched!)
Check if there is any match and if there is, it will proceed to send them a message from config.py
'''
def check_if_matched():
    log('***** check_if_matched START *****')
    matched = False
    time_between = extra.random_time()
    try:
        driver.implicitly_wait(5)
        send_message_to_match = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/a")
        keep_swiping = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div/button")
        log('***** Found Match!')

        if send_message_to_match:
            matched = True

    except NoSuchElementException:
        log('***** No matches! :(')

    if matched == True:
        send_message_to_match.click()
        log('***** Im inside the match chat!')

        time.sleep(time_between)

        chat_box = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/textarea") ## CHATbox
        line = config.message_to_send
        chat_box.send_keys(line[extra.random_pickup_line])
        log('***** Wrote message on chat_box')
        
        time.sleep(time_between)

        send_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/form/button")
        send_button.click()
        log('***** Message was sent!')

        time.sleep(time_between)

        exit = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/nav/a/div")
        exit.click()
        log('***** I have exited the match! and messaged succesfully')
        log('***** Will keep swiping!')
    else:
        log('***** No matches *****')
    log('***** check_if_matched END *****')

'''
(BONUS STEP)
Makes the bot to click around the pictures of each profile. Under development still
'''
def click_around():
    log('***** click_around START *****')
    driver.implicitly_wait(60)
    image = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]")
    time_between = extra.random_time()
    log("***** click_around() The time to wait is: " + str(time_between))
    time.sleep(time_between)
    image.click()
    exit = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/a[1]")
    log("***** Found exit!")
    log("***** Image clicked with time of: " + str(time_between))

    try:
        driver.implicitly_wait(5)
        next_pic = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/a[2]/div/div[2]/button[2]")
        log("***** Found next_pic")
    except NoSuchElementException:
        log("***** couldn't find anything")
        exit.click()
        log("***** Exited")
        return

    next_pic.click()
    log("***** Next image")
    time.sleep(1)
    exit.click()
    log("***** Exited")
    time.sleep(2)
    log('***** click_around END *****')

'''
(FINAL STEP)
Main logic is here. Likes and dislikes + calling other methods here
'''
def like():
    while True:
        log('***** like() Main function within script START ')
        try:
            driver.implicitly_wait(60)
            like = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[4]/span")
            dislike = driver.find_element(By.XPATH,"/html/body/div[1]/div/span/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[2]/span")
            time_between = extra.random_time()
            log("***** Like() The time to wait is: " + str(time_between))
            time.sleep(time_between)
            decision = extra.decision()
            log("***** Took decision: " + str(decision))
            if decision == 1:
                like.click()
                log("***** Liked! with decision: " + str(decision) + " and time in between : " + str(time_between))
                check_if_matched()
            elif decision == 0:
                dislike.click()
                log("***** Disliked! with decision: " + str(decision) + " and time in between : " + str(time_between))
        except NoSuchElementException:
            log("***** ERROR")
        log('***** like() Main function within script END *****')
            
if __name__ == "__main__":
    openTinder()
    driver.switch_to_window(driver.window_handles[-1])
    fbLogin()
    driver.switch_to_window(driver.window_handles[0])
    skip_intro()
    like()
    

