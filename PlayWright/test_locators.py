

from playwright.sync_api import Page, expect

def test_launch_url(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #time.sleep(5) # or
    page.wait_for_timeout(5000)
    #1. page.get_by_alt_text()
    logo=page.get_by_alt_text("company-branding")
    expect(logo).to_be_visible()

    #2. page.get_by_text()
    expect(page.get_by_text("Forgot your password?")).to_be_visible()   #full text
    #expect(page.get_by_text("Log")).to_be_visible()#partial text
    #expect(page.get_by_text(re.compile(".*ogi.*"))).to_be_visible()   #regular expression

    #3. page.get_by_role
    expect(page.get_by_role(role="heading",name="Login")).to_be_visible()

    #4. page.get_by_placeholder
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.wait_for_timeout(3000)
    #5. page.get_by_title
    #page.get_by_title("Username").to_have_text("user")
    page.get_by_role("button",name="Login").click()
    expect(page.get_by_role("heading",name="Dashboard")).to_have_text("Dashboard")
    print("Dashboard name is verified successfully")
    #tag.class
    page.locator("input.oxd-input").fill("Time")
    #tag.class[attribute='value']
    page.locator("a.oxd-main-menu-item.oxd-main-menu-item[href='/web/index.php/time/viewTimeModule']").click()
    #tag[attribute='value']
    page.locator("input[placeholder='Type for hints...']").fill("Ajay Kumar")
    page.wait_for_timeout(5000)
    