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
    page.get_by_role('link',name='iFrame').click()
    frame=page.frame_locator("#mce_0_ifr")
    print(frame.locator('p').inner_text())
    page.go_back()
    page.get_by_text("Nested Frames").click()
    print("hi")

    time.sleep(4)
