from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
options = Options()
options.headless = True
#driver = webdriver.Firefox(options=options, executable_path=r'E:\Downloads\geckodriver.exe')
driver = webdriver.Firefox(options=options, executable_path=r'/usr/bin/geckodriver')
driver.get("therandomurl")
time.sleep(10)
#driver.find_element_by_css_selector('button.mat-focus-indicator:nth-child(3)').click()
#time.sleep(2)
#driver.find_element_by_css_selector('#mat-input-0').send_keys("THEMAILSAC")
driver.find_element_by_css_selector('#mat-input-1').send_keys("THEMAILSAC")
driver.find_element_by_css_selector('#mat-input-2').send_keys("Xhzoamxtqyei1@gmail.com")
#driver.find_element_by_css_selector('#mat-input-3').send_keys("Xhzoamxtqyei1@gmail.com")
driver.find_element_by_css_selector('#continue-button').click()




#accept terms

driver.find_element_by_css_selector('#mat-checkbox-1 > label:nth-child(1) > div:nth-child(1)').click()
driver.find_element_by_css_selector('#mat-checkbox-2 > label:nth-child(1) > div:nth-child(1)').click()

driver.quit()