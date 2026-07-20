from playwright.sync_api import sync_playwright,Page,expect
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    browser_context=browser.new_context()
    page=browser.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    frame=page.get_by_text("Frames",exact=True)
    frame.scroll_into_view_if_needed()
    frame.click()
    time.sleep(4)
