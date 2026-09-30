from playwright.sync_api import Page, expect
"""
def test_radio(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    gender_text=page.get_by_text("Gender:")
    #verify gender label is visible or not
    expect(gender_text).to_be_visible()
    male=page.locator("#male")
    # verify male radio is unchecked defaultly
    expect(male).not_to_be_checked()
    male.check()
    # verify female radio is unchecked defaultly
    female = page.locator("#female")
    expect(female).not_to_be_checked()
    female.check()
    page.wait_for_timeout(5000)
"""
def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)
    #check the specific checkbox
    page.get_by_text("Sunday").check()
    page.wait_for_timeout(5000)


