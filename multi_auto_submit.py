from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from secrets import userid, userpwd
import csv
from urllib.parse import urlencode
request_text = ""
browser = webdriver.Chrome() # ('~/development/PROD/assets/chromedriver')  # Optional argument, if not specified will search path.


def log_in ():
	browser.get("https://www.whatdotheyknow.com/profile/sign_in") 
	time.sleep(5)
	username = browser.find_element_by_id("user_signin_email")
	password = browser.find_element_by_id("user_signin_password")
	username.send_keys(userid)
	password.send_keys(userpwd)
	time.sleep(3)
	login_attempt = browser.find_element_by_xpath("//*[@value='Sign in']")
	login_attempt.submit()

def make_request(intext):
	fulltext = ""
	fulltext = "https://www.whatdotheyknow.com/new/aberdeen_city_council?" + intext
	browser.get(fulltext) 

	time.sleep(3)

	preview_request = browser.find_element_by_xpath("//*[@value='Preview your public request']")
	preview_request.submit()

	time.sleep (3)

	submit_request = browser.find_element_by_xpath("//*[@value='Send and publish request']")
	submit_request.submit()

def log_out():
	pass


def url_encode(in_dict):
	x = urlencode(in_dict)
	return x

title_text = 'Speeding in 20mph areas'
preamble = 'Please provide '
letter_text = "a list of the number of people fined for speeding in either mandatory (red) or recommended (green) 20mph in each zone of Aberdeen, monthly for the last 24 months in CSV format . "
More_info = 'More info: https://tinyurl.com/ycysjqls' + "\n" + "George Smith"
tag_text = 'ODIAberdeen CTC11'

#main code starts here
outtext = {'title': title_text, 'default_letter': preamble+letter_text+More_info, 'tags': tag_text}
reqtext = url_encode(outtext)


#get_data()

log_in()

make_request(reqtext)

#log_out()


