
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import sys
from anticaptchaofficial.imagecaptcha import *

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r'/Users/devanshu/Documents/chromedriver',chrome_options=options)
url = 'https://uims.cuchd.in/uims/'

username= "21MCI1009"
password= "12345#Change"
driver.get(url)
driver.find_element_by_id("txtUserId").send_keys(username)
driver.find_element_by_id("btnNext").click()
driver.implicitly_wait(2)


driver.find_element_by_id("txtLoginPassword").send_keys(password)
reload= False
if(reload):
        driver.find_element_by_id("lnkupCaptchalnkupCaptcha").click()
        time.sleep(1)
a = driver.find_element_by_id('imgCaptcha')
a.screenshot("cap.png")
solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("64583d0034201dce72bb4772631fd3ef")
solver.set_soft_id(0)
captcha_text = solver.solve_and_return_solution("cap.png")
if captcha_text != 0:
    driver.find_element_by_id("txtcaptcha").send_keys(captcha_text)
    driver.find_element_by_id("btnLogin").click()
    print("Captcha Done",captcha_text)
else:
    print("task finished with error "+solver.error_code)
    reload = True
