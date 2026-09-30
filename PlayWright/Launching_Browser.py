from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = browser.new_page()
    page.goto("https://www.facebook.com")
    input("enter to close the page")
