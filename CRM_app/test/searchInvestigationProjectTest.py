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

class SearchInvestigationProyectest(LiveServerTestCase):

    def test(self):

        selenium = login(self)

        allies = selenium.find_element("id", "allies")
        allies.click()
        
        ally = selenium.find_element("id", "123456")
        ally.click()

        projects = selenium.find_element("id", "projects")
        projects.click()

        time.sleep(2)

        search = selenium.find_element("name", "q")
        search.send_keys("investiga")

        time.sleep(2)

        searchbtn = selenium.find_element(By.XPATH, "//b[contains(.,'Buscar')]")
        searchbtn.click()

        time.sleep(2)

        checkProject = selenium.find_element(By.XPATH, "//div[2]/a/img")

        assert checkProject != None

        selenium.quit

