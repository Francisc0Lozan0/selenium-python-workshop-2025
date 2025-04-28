from behave import given, then, when
from selenium import webdriver

from pages.wiki_title_page import WikiTitle


@given('I am on the Wikipedia page for python')
def step_given_wiki_title(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://es.wikipedia.org/wiki/Python")
    context.wiki_title_page = WikiTitle(context.driver)



@when('I check the title of the page')
def when_wiki_title(context):
    context.wiki_title_page.get_title()
    assert "Python" == context.wiki_title_page.isElementPresent()
    

@then('the title should be Python')
def then_wiki_title(context):
    context.wiki_title_page.get_title()
    assert "Python" == context.wiki_title_page.isElementPresent()