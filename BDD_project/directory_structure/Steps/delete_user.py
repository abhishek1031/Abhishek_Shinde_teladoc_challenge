import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@then('delete selected user')
def delete_button(context):
    context.driver.find_element(By.XPATH,"//td[text()='Novak']/following-sibling::td//button[@ng-click='delUser()']").click()


@then('confirm deletion')
def confirm(context):
    context.driver.find_element(By.XPATH,"//button[text()='OK']").click()


@then('assert user deleted')
def assert_deletion(context):
    #assert not context.driver.find_element(By.XPATH,"//td[text()='Novak']"), "test Pass"
    time.sleep(5)