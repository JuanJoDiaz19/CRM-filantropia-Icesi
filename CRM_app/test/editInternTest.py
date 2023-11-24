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

class EditInternTest(LiveServerTestCase):

    def test(self):

        selenium = login(self)

        allies = selenium.find_element("id", "allies")
        allies.click()

        ally = selenium.find_element("id", "123456")
        ally.click()

        intern = selenium.find_element("id", "interns")
        intern.click()

        time.sleep(3)

        checkIntern = selenium.find_element("id", "1346752")
        checkIntern.click()

        time.sleep(2)

        name = selenium.find_element("name", "nombre")
        select_element = selenium.find_element("name", "allie_area")
        description = selenium.find_element("name", "allie_description")
        img = selenium.find_element("id", "customFileInput")

        name.clear()
        name.send_keys("LONDOÑO SOFIA ANA")

        select = Select(select_element)
        select.select_by_visible_text("Quimica Farmaceutica")

        description.clear()
        description.send_keys("ESTA DESCRIPCION FUE EDITADA.")
        
        imgpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img', 'googlelogo.jpeg'))
        img.clear()
        img.send_keys(imgpath)

        edit = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.NAME, "edit"))
        )

        selenium.execute_script("arguments[0].scrollIntoView(true);", edit)
        selenium.execute_script("arguments[0].click();", edit)

        time.sleep(2)

        checkIntern = selenium.find_element("id", "1346752")
        checkIntern.click()

        time.sleep(2)

        name = selenium.find_element("name", "nombre")
        select_element = selenium.find_element("name", "allie_area")
        select = Select(select_element)
        area = select.first_selected_option.text
        description = selenium.find_element("name", "allie_description")

        assert name.get_attribute('value') == "LONDOÑO SOFIA ANA"
        assert description.text == "ESTA DESCRIPCION FUE EDITADA."
        assert area == "Quimica Farmaceutica"

        time.sleep(2)

        selenium.quit

