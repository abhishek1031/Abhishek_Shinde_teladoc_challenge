import logging

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#driver=webdriver.Chrome()
#driver.find_element().send_keys()
@given('Launch the Chrome Browser')
def launch_browser(context):
    context.driver= webdriver.Chrome()


@when('open given url')
def openUrl(context):
    context.driver.get("https://www.way2automation.com/angularjs-protractor/webtables/")
    context.driver.maximize_window()
    time.sleep(2)


@then('click on add user button')
def add_button(context):
    context.driver.find_element(By.XPATH,"//button[@class='btn btn-link pull-right']").click()


@then('add user details')
def user_details(context):
    context.driver.find_element(By.XPATH, "//input[@name='FirstName']").send_keys("abhishek")
    context.driver.find_element(By.XPATH, "//input[@name='LastName']").send_keys("abhishek")
    context.driver.find_element(By.XPATH, "//input[@name='UserName']").send_keys("abhishek")
    context.driver.find_element(By.XPATH, "//input[@name='Password']").send_keys("abhishek")
    select=Select(context.driver.find_element(By.XPATH,"//select"))
    select.select_by_index(1)
    context.driver.find_element(By.XPATH, "//input[@name='Email']").send_keys("abhishek@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@name='Mobilephone']").send_keys("8087982591")


@then('click on save button')
def save_details(context):
    context.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()



@then('assert user added')
def verify_user_addition(context):
    assert context.driver.find_element(By.XPATH,"//td[text()='abhishek']"), "test Pass"



@then('close browser')
def close_browser(context):
    pass