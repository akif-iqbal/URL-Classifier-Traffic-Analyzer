import webbrowser
from selenium import webdriver

# optionss = webdriver.ChromeOptions()
# optionss.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=optionss)

driver = webdriver.Chrome()
driver.get("http://www.liquidgeneration.com")
print(driver.current_url)
#driver.quit()