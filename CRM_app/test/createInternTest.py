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

class EditAllyTest(LiveServerTestCase):

    def test(self):

        selenium = login(self)

        allies = selenium.find_element("id", "allies")
        allies.click()

        ally = selenium.find_element("id", "123456")
        ally.click()

        intern = selenium.find_element("id", "interns")
        intern.click()

        time.sleep(1)

        add = selenium.find_element("id", "add")
        add.click()

        name = selenium.find_element("name", "nombre")
        sex = selenium.find_element("id", "m")
        id = selenium.find_element("name", "allie_document_id")
        area = selenium.find_element("name", "allie_area")
        imgpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img', 'test.png'))
        img = selenium.find_element("id", "customFileInput")
        description = selenium.find_element("id", "expanding-input")

        name.send_keys("test")
        sex.click()
        id.send_keys("123")
        select = Select(area)
        select.select_by_visible_text("Quimica Farmaceutica")
        img.send_keys(imgpath)
        description.send_keys("testing")
        
        submit = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )

        time.sleep(2)

        selenium.execute_script("arguments[0].scrollIntoView(true);", submit)
        selenium.execute_script("arguments[0].click();", submit)

        checkintern = selenium.find_element("id", "123")

        assert checkintern != None

        time.sleep(3)

        selenium.quit

