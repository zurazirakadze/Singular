from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False, 'profile.default_content_setting_values.geolocation': 2,
    'profile': {
        'password_manager_enabled': False
    }
})

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)


def findElement(by):
    return driver.find_element(*by)


def findElements(by):
    return driver.find_elements(*by)








