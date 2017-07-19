from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import os

def netbet_scrapping():

	display = Display(visible = 0, size = (1200, 900))
	display.start()
	try:
		Netbet = webdriver.Chrome(executable_path=os.path.abspath("/usr/bin/chromedriver"))
		Netbet.get("https://www.livepartners.com/")
		Netbet.find_element_by_css_selector("#top > div > a").click()
		Netbet.implicitly_wait(10)
		Netbet.find_element_by_id("login_username").send_keys("betfyuk")
		Netbet.find_element_by_id("login_password").send_keys("dontfuckwithme")
		pwd = Netbet.find_element_by_id("login_password")
		pwd.send_keys(Keys.RETURN)
		Netbet.implicitly_wait(10)
		balance = Netbet.find_element_by_xpath("//*[@id='contentwrapper']/div/div[1]/div[2]/div/strong").text
		return balance
	finally:
		Netbet.quit()
		display.stop()

