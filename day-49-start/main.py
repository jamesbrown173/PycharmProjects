from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
time.sleep(10)
user_name = driver.find_element(By.ID, "username")
user_name.send_keys('jamesbrown173@gmail.com')
time.sleep(10)
password = driver.find_element(By.ID, "password")
password.send_keys('Minoxidil12')
time.sleep(10)
password.send_keys(Keys.ENTER)


#
# < input
# id = "username"
# name = "session_key"
# type = "text"
# aria - describedby = "error-for-username"
# required = ""
# validation = "email|tel"
# class ="" autofocus="" aria-label="Email or Phone" autocomplete="webauthn">

# <a class="nav__button-secondary btn-md btn-secondary-emphasis" href="https://www.linkedin.com/login?emailAddress=&amp;fromSignIn=&amp;fromSignIn=true&amp;session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3Ff_LF%3Df_AL%26geoId%3D102257491%26keywords%3Dpython%2520developer%26location%3DLondon%252C%2520England%252C%2520United%2520Kingdom%26redirect%3Dfalse%26position%3D1%26pageNum%3D0&amp;trk=public_jobs_nav-header-signin" data-tracking-control-name="public_jobs_nav-header-signin" data-tracking-will-navigate="">
#            Sign in
#        </a>
#



# driver.close()
