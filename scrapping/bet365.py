from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
import os


def bet365_scrapping():
	display = Display(visible=0, size=(1200, 900))
	display.start()
	try:
		bet365 = webdriver.Chrome(executable_path=os.path.abspath("/usr/bin/chromedriver"))
		bet365.get("https://www.bet365affiliates.com/ui/pages/affiliates/Affiliates.aspx")
		assert "bet365" in bet365.title
		user = bet365.find_element_by_css_selector("input[name='ctl00$MasterHeaderPlaceHolder$ctl00$userNameTextbox']")
		user.clear()
		user.send_keys("betfyuk")	
		pwd =bet365.find_element_by_id("ctl00_MasterHeaderPlaceHolder_ctl00_tempPasswordTextbox") 
		pwd.clear() 
		pwd =bet365.find_element_by_css_selector("#ctl00_MasterHeaderPlaceHolder_ctl00_passwordTextbox") 
		pwd.send_keys("passiveincome") 
		pwd.send_keys(Keys.RETURN)
		bet365.implicitly_wait(10)
		balance = bet365.find_element_by_link_text("Show Balance")
		balance.click() 
		bet365.implicitly_wait(20)
		window_after = bet365.window_handles[1]
		bet365.switch_to_window(window_after)
		incomes_arr = []
		for incomes in bet365.find_elements_by_class_name("rgt"):
			if incomes.text != "Close Window":
				incomes_arr.append(incomes.text)
		return incomes_arr
	finally:
		bet365.quit()
		display.stop()