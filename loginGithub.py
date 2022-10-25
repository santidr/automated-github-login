from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

username = os.environ.get('my-user')
password = os.environ.get('my-pass')

user_agent = os.environ.get('user-agent')
driver_path = os.environ.get('driver-path')

url = 'https://github.com/'

opts = Options()
opts.add_argument(f'user-agent={user_agent}')

driver = webdriver.Edge(driver_path, options=opts)

driver.get(url)

driver.maximize_window()
sleep(1)
driver.find_element(By.XPATH, '//body/div[1]/header/div/div[2]/div/div/div[2]/a').click()
sleep(1)
driver.find_element(By.ID, 'login_field').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
sleep(1)
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').click()

print('Logged in successfully!')