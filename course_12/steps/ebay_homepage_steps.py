from behave import *
"""
features -> features: scenarios

pages -> definite metodele
clasele din pages mostenesc base page
dupa ce am creat pagina, mergem in environment si instantiem un obiect de tip page-ul(clasa) pe care l-am creat

"""

@given("Home page: I am on ebay homepage")
def step_impl(context):
    context.home_page_object.navigate_to_homepage()
    context.home_page_object.accept_cookies()

@when('Home page: I search for "{product_name}"  from category "{category_name}"')
def step_impl(context, product_name, category_name):
    context.home_page_object. insert_search_value(product_name)
    context.home_page_object.chose_category(category_name)
    context.home_page_object.click_search_button()

@then('Home page: I received as a results also iPhone8 64GB')
def step_impl(context):
    context.home_page_object.check_search_results()

@when('Home page: I click on the advanced link')
def step_impl(context):
    context.home_page_object.click_advanced_search_link()



