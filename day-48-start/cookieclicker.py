from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")



# Chooses the language at the start
driver.implicitly_wait(300)
language_choice = driver.find_element(By.ID, 'langSelect-EN')
language_choice.click()


# Clicks the big cookie
driver.implicitly_wait(300)
cookie = driver.find_element(By.ID, 'bigCookie')
print(cookie)
# cookie.click()




# <div class="langSelectButton title" style="padding:4px;" id="langSelect-EN">English</div>