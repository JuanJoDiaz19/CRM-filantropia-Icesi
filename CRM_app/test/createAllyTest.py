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
    
class AddAllyTest(LiveServerTestCase):

    def test(self):

        selenium = login(self)

        allies = selenium.find_element("id", "allies")

        allies.click()

        add = selenium.find_element("id", "add")

        add.click()

        time.sleep(2)

        name = selenium.find_element("name", "allie_name")
        allyType = selenium.find_element("id", "ally_typej")
        id = selenium.find_element("name", "allie_document_id")
        description = selenium.find_element("id", "expanding-input")
        img = selenium.find_element("id", "customFileInput")
        imgpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'img', 'googlelogo.jpeg'))

        select_element = selenium.find_element("name", "allie_area")
        select = Select(select_element)
        select.select_by_visible_text("Finanzas")

        name.send_keys("GOOGLE")
        allyType.click()
        id.send_keys("12343")
        description.send_keys("12345")
        img.send_keys(imgpath)

        time.sleep(2)

        contactName = selenium.find_element("name", "contact_name")
        contactid = selenium.find_element("name", "contact_document_id")
        contactEmail = selenium.find_element("name", "contact_email")
        contactAuxEmail = selenium.find_element("name", "contact_aux_email")
        contactPhone = selenium.find_element("name", "contact_phone")
        submit = selenium.find_element("id", "submit")

        contactName.send_keys("aaa")
        contactid.send_keys("223")
        contactEmail.send_keys("1234@123.com")
        contactAuxEmail.send_keys("1234@122.com")
        contactPhone.send_keys("1112")

        time.sleep(2)

        submit = WebDriverWait(selenium, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )

        selenium.execute_script("arguments[0].scrollIntoView(true);", submit)
        selenium.execute_script("arguments[0].click();", submit)

        selenium.get("http://127.0.0.1:8000/allies")

        checkAlly = selenium.find_element("id", "12343")

        assert checkAlly != None

        time.sleep(4)

        selenium.quit



        






