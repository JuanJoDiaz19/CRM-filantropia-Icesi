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

        time.sleep(2)

        edit = selenium.find_element("id", "edit")
        edit.click()

        time.sleep(2)

        name = selenium.find_element("name", "allie_name")
        name.clear()
        name.send_keys("Perfection")

        select_element = selenium.find_element("name", "allie_area")
        select = Select(select_element)
        select.select_by_visible_text("Finanzas")

        description = selenium.find_element("name", "allie_description")
        description.clear()
        description.send_keys("HOLA ESTO FUE EDITADO.")

        img = selenium.find_element("id", "customFileInput")
        imgpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img', 'googlelogo.jpeg'))
        img.clear()
        img.send_keys(imgpath)

        time.sleep(2)

        confirm = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm"))
        )

        selenium.execute_script("arguments[0].scrollIntoView(true);", confirm)
        selenium.execute_script("arguments[0].click();", confirm)

        time.sleep(2)

        name = selenium.find_element("id", "name").text
        area = selenium.find_element("id", "area").text
        description = selenium.find_element("id", "description").text

        assert name == "Perfection"
        assert area == "Finanzas"
        assert description == "HOLA ESTO FUE EDITADO."

        selenium.quit

