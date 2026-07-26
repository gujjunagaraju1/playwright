from playwright.sync_api import Page,expect
from playwright.sync_api import sync_playwright
import time


#auth for popups
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context(
        http_credentials={
            "username":"admin",
            "password":"admin"
        }
    )
    page=context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.go_back()
    time.sleep(4)
