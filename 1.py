
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#driver = webdriver.Firefox

driver=webdriver.Chrome()
#wait = WebDriverWait(driver, 20)

#driver.implicitly_wait(20) # seconds

#driver.get("http://somedomain/url_that_delays_loading")
#myDynamicElement = driver.find_element_by_id("myDynamicElement")

driver.get('http://www.python.org')

assert 'Python' in driver.title
elem=driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
assert "No results Found." not in driver.page_sourse
driver.close()
