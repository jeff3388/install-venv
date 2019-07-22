from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(profile)

driver.get("http://www.binarymanaic.com")

print(driver.title)

driver = webdriver.Firefox()