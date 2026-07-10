from playwright.sync_api import Page,expect
import time

def test_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",wait_until="domcontentloaded")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    time.sleep(2)
    expect(page.get_by_alt_text("client brand banner")).to_be_visible()
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()
    page.close()