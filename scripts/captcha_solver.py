from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By

def solve_captcha(url):
    driver = Chrome(headless=True)
    driver.get(url)
    driver.execute_script('''
        document.querySelector('iframe[src*="cloudflare"]')
               .contentDocument.querySelector("#checkbox").click();
    ''')
    time.sleep(5)  # Allow challenge
    return driver.get_cookie('cf_clearance')
