from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from selenium import webdriver
import os

display = Display(visible=0, size=(800, 600))
display.start()

chromedriver='/usr/lib/chromium-browser/chromedriver'
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress",  "localhost:9222")
os.environ["webdriver.chrome.driver"]=chromedriver
driver = webdriver.Chrome(executable_path=chromedriver)

driver.get("http://www.binarymanaic.com")

print(driver.title)

driver.close()
driver.quit()

