from autoswiper import TinderBot

email = input('Enter FB Email: ')
password = input('Enter Password: ') 

obj = TinderBot(email,password)
obj.start()
