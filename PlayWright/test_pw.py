from playwright.sync_api import Page, expect

def test_launchUrl(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    myUrl=page.url
    print("application URL: ", myUrl)
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")





"""
from playwright.sync_api import Page, expect

def test_verifyPageUrl(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")      #launch url  passing url
    MyUrl=page.url      #  to get the Url
    print("The application of the URL is",MyUrl)
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")    #verifying  expected url

def test_verifyTitle(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    MyTitle = page.title()   # to get the title of the page
    print("The application of the Title is", MyTitle)
    expect(page).to_have_title("OrangeHRM")
"""