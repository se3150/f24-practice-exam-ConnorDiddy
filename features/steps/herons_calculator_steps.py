from behave import given, step, then, when
from selenium.webdriver.common.keys import Keys

@given (u'I open the url "{url}"')
def step_impl(context, url):
    context.behave_driver.open_url(url)
    
@then(u'I should see the search bar')
def step_impl(context):
    # search for an input element with placeholder text "Search"
    search_bar = context.behave_driver.get_element("input[placeholder='Search']")
    assert search_bar is not None
    
@given(u'I enter the sides of the triangle as {side1}, {side2}, {side3}')
def step_impl(context, side1, side2, side3):
    side1_field = context.behave_driver.get_element("input#a")
    side2_field = context.behave_driver.get_element("input#b")
    side3_field = context.behave_driver.get_element("input#c")
    
    side1_field.clear()
    side1_field.send_keys(side1)
    
    side2_field.clear()
    side2_field.send_keys(side2)
    
    side3_field.clear()
    side3_field.send_keys(side3)
    
    
@when(u'I click on the calculate button')
def step_impl(context):
    calculate_button = context.behave_driver.get_element("input.clcbtn")
    calculate_button.click()
    

@then(u'I should see the area of the triangle as {result}')
def step_impl(context, result):
    result_field = context.behave_driver.get_element("input#_d")
    assert result_field.get_attribute("value") == result
    context.behave_driver.pause(1000)