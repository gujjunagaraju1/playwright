from playwright.sync_api import Page,expect, sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_text("kaneqafile.txt").click()
    download=download_info.value
    download.save_as("kaneqafile.txt")
   