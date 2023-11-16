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

class CreateInvestigationProject(LiveServerTestCase):

    def test(self):

        selenium = login(self)

        allies = selenium.find_element("id", "allies")
        allies.click()
        
        ally = selenium.find_element("id", "123456")
        ally.click()

        projects = selenium.find_element("id", "projects")
        projects.click()

        time.sleep(2)

        add = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[2]/a/img"))
        )

        selenium.execute_script("arguments[0].scrollIntoView(true);", add)
        selenium.execute_script("arguments[0].click();", add)

        title = selenium.find_element("name", "titulo")
        date = selenium.find_element("name", "fecha")

        time.sleep(2)

        description = selenium.find_element("name", "descripcion")
        objectives = selenium.find_element("name", "objetivos")

        title.send_keys("TEST")
        date.send_keys("2023-11-17")
        description.send_keys("TEST")
        objectives.send_keys("TEST")

        time.sleep(2)

        submit = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.NAME, "submit"))
        )

        selenium.execute_script("arguments[0].scrollIntoView(true);", submit)
        selenium.execute_script("arguments[0].click();", submit)

        time.sleep(2)




        selenium.quit

