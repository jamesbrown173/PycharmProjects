from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

parent_div = driver.find_element(By.CLASS_NAME, 'event-widget')

date = parent_div.find_elements(By.TAG_NAME, "time")
event_title = parent_div.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_title)):
    events[n] = {
        "time": date[n].text,
        "name": event_title[n].text
    }

print(events)
driver.close()


##############################################################################################


## How to input text
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


## Search by link text
# community_portal = driver.find_element(By.LINK_TEXT,"Community portal")
# print(community_portal.get_attribute("href"))


## Find by CSS Selector
# date = parent_div.find_elements(By.TAG_NAME, "time")
# event_title = parent_div.find_elements(By.CSS_SELECTOR, ".event-widget li a")