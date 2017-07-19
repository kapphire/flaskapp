from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import os


def coral_scrapping():
	display = Display(visible = 0, size = (1200, 900))
	display.start()

	try:
		Coral = webdriver.Chrome(executable_path=os.path.abspath("/usr/bin/chromedriver"))
		Coral.get("http://affiliates.coral.co.uk/")
		Coral.find_element_by_link_text("Log In").click()
		window_after = Coral.window_handles[1]
		Coral.switch_to_window(window_after)
		Coral.find_element_by_id("username").send_keys("betfyuk1")
		Coral.find_element_by_id("password").send_keys("dontfuckwithme")
		pwd = Coral.find_element_by_id("password")
		pwd.send_keys(Keys.RETURN)
		Coral.implicitly_wait(10)
		mtd_valArr = []
		table = Coral.find_element(by=By.ID, value = "dashboard_quick_stats")
		mtds_val = Coral.find_element(by=By.CLASS_NAME, value = "row_light_color")
		for mtd_val in mtds_val.find_elements_by_tag_name("td"):
			mtd_valArr.append(mtd_val.text)
		return mtd_valArr
	finally:
		Coral.quit()
		display.stop()	