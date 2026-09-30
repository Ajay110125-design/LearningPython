from playwright.sync_api import Page, expect

def test_verifyactions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    name=page.locator("#name")
    #verify element is visible/enabled
    expect(name).to_be_visible()
    expect(name).to_be_enabled()
    #check the attribute of the element
    expect(name).to_have_attribute("maxlength","15")
    #get the attribute of the element
    maxlength=name.get_attribute("maxlength")
    print("maxlength:", maxlength)
    #fill the element
    name.fill("Ajay Kumar")
    #get the input value from the input box
    enteredname=name.input_value()
    print("Entered value is ",enteredname)
    page.wait_for_timeout(5000)



