from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 50
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"

service = Service("/Users/kaian/Documents/Development/chromedriver.exe")


class InternetSpeedTwitterbot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                                '/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        down_speed = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                                 '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]'
                                                                 '/div[2]/div/div[2]/span')
        up_speed = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]'
                                                               '/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]'
                                                               '/div/div[2]/span')
        self.down = down_speed.get_attribute("innerText")
        self.up = up_speed.get_attribute("innerText")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        sign_in = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]'
                                                              '/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(2)
        email = self.driver.find_element(by=By.NAME, value='text')
        email.click()
        email.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        # time.sleep(5)
        # unusual logins
        # username = self.driver.find_element(by=By.NAME, value='text')
        # username.send_keys("kvikvne")
        # time.sleep(5)
        # username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        tweet_text = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_text.send_keys(f"i am a bot uWu")


bot = InternetSpeedTwitterbot(service)
# bot.get_internet_speed()
bot.tweet_at_provider()
