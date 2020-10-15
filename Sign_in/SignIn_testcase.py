from selenium.webdriver.common.keys import Keys
from behave_webdriver.steps import *
from Helper.def_helper import *
from Page_Obj.pageobjects import *


def authorization(user, Pass):
    driver.get(singulardev)
    findElement(username).send_keys(str(user))
    findElement(password).send_keys(str(Pass), Keys.ENTER)
    #findElement(login).click()
