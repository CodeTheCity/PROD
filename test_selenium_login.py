from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from secrets import userid, userpwd

browser = webdriver.Chrome() # ('~/development/PROD/assets/chromedriver')  # Optional argument, if not specified will search path.
browser.get("https://www.whatdotheyknow.com/profile/sign_in") 
time.sleep(10)
username = browser.find_element_by_id("user_signin_email")
password = browser.find_element_by_id("user_signin_password")
username.send_keys(userid)
password.send_keys(userpwd)
time.sleep(10)
login_attempt = browser.find_element_by_xpath("//*[@value='Sign in']")
login_attempt.submit()

new_request = "https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)"
browser.get(new_request) 

time.sleep(10)

preview_request = browser.find_element_by_xpath("//*[@value='Preview your public request']")
preview_request.submit()

time.sleep (10)

submit_request = browser.find_element_by_xpath("//*[@value='Send and publish request']")
#submit_request.submit()
