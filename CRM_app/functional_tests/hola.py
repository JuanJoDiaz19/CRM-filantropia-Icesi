from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

selenium = webdriver.Chrome()

selenium.get("http://127.0.0.1:8000/")

username = selenium.find_element("id",'username')
password = selenium.find_element("id",'password')
submit = selenium.find_element("id",'submit')

username.send_keys('123')
password.send_keys('123')
submit.send_keys(Keys.RETURN)

