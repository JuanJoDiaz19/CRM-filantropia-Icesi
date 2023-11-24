from django.test import LiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import time     
import os

def login(self):
    selenium = webdriver.Chrome()

    selenium.get("http://127.0.0.1:8000/")

    username = selenium.find_element("id",'username')
    password = selenium.find_element("id",'password')
    submit = selenium.find_element("id",'submit')

    username.send_keys('1234')
    password.send_keys('1234')
    submit.click()

    return selenium

class SearchInternTest(LiveServerTestCase):

    def test(self):

        selenium = login(self)

        allies = selenium.find_element("id", "allies")
        allies.click()

        ally = selenium.find_element("id", "123456")
        ally.click()

        intern = selenium.find_element("id", "interns")
        intern.click()

        time.sleep(1)

        search = selenium.find_element("id", "searchText")
        searchbtn = selenium.find_element("id", "find")

        search.send_keys("ana")

        searchbtn.click()

        time.sleep(3)

        checkIntern = selenium.find_element("id", "1346752")

        assert checkIntern != None

        selenium.quit

