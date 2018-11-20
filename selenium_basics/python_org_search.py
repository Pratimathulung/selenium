import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Welcome to Python.org" == driver.title
# assert "Welcome to Python.org1" == driver.title
time.sleep(2)

search_bar = driver.find_element_by_id('id-search-field')
search_bar.clear()
search_bar.send_keys('Pratima')
time.sleep(2)
search_bar.send_keys(Keys.RETURN)
assert 'No results found.' in driver.page_source
time.sleep(2)
driver.close()


