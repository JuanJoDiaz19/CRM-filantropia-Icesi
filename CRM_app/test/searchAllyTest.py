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

class SearchAllyTest(LiveServerTestCase):

    def test(self):
        
        selenium = login(self)

        allies = selenium.find_element("id", "allies")

        allies.click()

        element_to_scroll = selenium.find_element("id", 'allyContainer')

        wait = WebDriverWait(selenium, 10)
        wait.until(EC.visibility_of(element_to_scroll))

        selenium.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element_to_scroll)

        select_element = selenium.find_element("name", "estado")
        state = Select(select_element)
        state.select_by_visible_text("Inactivo")

        search = selenium.find_element("id", "search")

        select_element2 = selenium.find_element("name", "tipo")
        type = Select(select_element2)
        type.select_by_visible_text("Todos")

        time.sleep(1)

        try:
            search.click()
        except StaleElementReferenceException:
            search = selenium.find_element("id", "search")
            search.click()

        time.sleep(1)

        select_element = selenium.find_element("name", "estado")
        state = Select(select_element)
        state.select_by_visible_text("Todos")

        select_element2 = selenium.find_element("name", "tipo")
        type = Select(select_element2)
        type.select_by_visible_text("Juridico")

        time.sleep(1)

        try:
            search.click()
        except StaleElementReferenceException:
            search = selenium.find_element("id", "search")
            search.click()

        time.sleep(1)

        name = selenium.find_element("name", "q")

        name.send_keys("Perfic")

        time.sleep(1)

        try:
            search.click()
        except StaleElementReferenceException:
            search = selenium.find_element("id", "search")
            search.click()

        time.sleep(1)

        name = selenium.find_element("name", "q")

        name.clear()

        name.send_keys("nada")

        time.sleep(1)

        try:
            search.click()
        except StaleElementReferenceException:
            search = selenium.find_element("id", "search")
            search.click()

        time.sleep(1)

        selenium.quit()

