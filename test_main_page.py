from .pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By

#pytest -v --tb=line --language=en-gb test_main_page.py
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
