from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")

#if headless:
#    options.headless = True

driver = webdriver.Chrome(options=options)

start_url = 'https://code-maven.com/'
driver.get(start_url)
assert driver.title == 'Code Maven - for people who code'
driver.close()
