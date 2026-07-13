from playwright.sync_api import Page,expect
import time
from config.config import config
from page.loginPage import loginPage

def test_login(page:Page):

    page.goto(config.BaseUrl,wait_until="domcontentloaded")
    loginPages=loginPage(page)
    loginPages.login(config.userName,config.password)
    
    '''page.get_by_placeholder("Username").fill(config.userName)
    page.get_by_placeholder("Password").fill(config.password)
    page.get_by_role("button",name="Login").click()
    time.sleep(2)'''
    expect(page.get_by_alt_text("client brand banner")).to_be_visible()
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()
    page.close()