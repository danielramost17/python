from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
import time

usernameStr = ''
passwordStr = ''
nome = ''
message = "Hey 'put some name here', what's up? It's not me who's sending this, it's a bot I programmed."

options = Options()
options.add_argument("--disable-notifications")
browser = webdriver.Chrome('/home/daniel/pycharm-community-2016.3.2/chromedriver', chrome_options=options)
browser.get('https://www.facebook.com/')

username = browser.find_element_by_id('email')
username.send_keys(usernameStr)
password = browser.find_element_by_id('pass')
password.send_keys(passwordStr)
signInButton = browser.find_element_by_id('u_0_r')
signInButton.click()
time.sleep(5)

pesquisar = browser.find_element_by_x_path('//*[@id="u_0_2a"]/div/div[2]/span/label/input')
pesquisar.send_keys(nome)
pessoa = browser.find_element_by_class_name('_364g')
pessoa.click()
chat = browser.find_element_by_class_name('_1mj')
chat.send_keys(message)
chat.send_keys(keys.Keys.ENTER)

browser.quit()