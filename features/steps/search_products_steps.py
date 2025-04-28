from behave import given, when, then
from selenium import webdriver
from pages.search_product_page import Search


@given('el usuario se encuentra en la pagina de MercadoLibre')
def step_given_MercadoLibre_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co')
    context.search_product_page = Search(context.driver)


@when('el usuario escribe el nombre de un producto')
def step_when_type_product(context):
    context.search_product_page.search_product("iPhone 13")


@then('muestra productos')
def step_then_see_product(context):
    assert "Iphone" == context.search_product_page.isElementPresent()

