from selenium import webdriver

import time

driver = webdriver.Chrome('E:\project\AUTOMATION\chromedriver.exe')
driver.maximize_window()

time.sleep(2)
driver.get('https://www.google.com/search?q=spider+man+no+way+home&oq=spider+man+no+way+home&aqs=chrome..69i57.5897j0j7&sourceid=chrome&ie=UTF-8')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div/a/div/div[2]/div[1]/div').click()

time.sleep(5)
driver.find_elements_by_name('search_query').send_keys('Marvel Eternals')
time.sleep(5)
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon').click()
driver.refresh()
driver.title()
driver.close()
