from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('https://unisat.io/market/brc20?tick=Oshi')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "usd")))
element = driver.find_element(By.XPATH, '//div[contains(@class, "price-line")]/span[contains(@class, "usd")]')
print(element.text)

xpath = "//*[@id='rc-tabs-0-panel-1']/div/div/div[1]/div[2]/div[3]/span[1]"
wait = WebDriverWait(driver, 10)

price = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

price = driver.find_element(By.XPATH,xpath)

print(price.text)

driver.quit()
