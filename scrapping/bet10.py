from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import os


def bet10_scrapping():
	display = Display(visible=0, size=(1200, 900))
	display.start()
	try:		
		bet10 = webdriver.Chrome(executable_path=os.path.abspath("/usr/bin/chromedriver"))
		bet10.get("http://partners.10bet.com/")
		bet10.find_element_by_id("username").send_keys("betfyuk")
		bet10.find_element_by_id("password").send_keys("dontfuckwithme")
		pwd = bet10.find_element_by_id("password")
		pwd.send_keys(Keys.RETURN)
		bet10.implicitly_wait(10)
		mtd_valArr = []
		table = bet10.find_element(by=By.ID, value = "dashboard_quick_stats")
		mtds_val = table.find_element(by=By.CLASS_NAME, value = "row_light_color")
		for mtd_val in mtds_val.find_elements_by_tag_name("td"):
			mtd_valArr.append(mtd_val.text)
		return mtd_valArr
	finally:
		bet10.quit()
		display.stop()

