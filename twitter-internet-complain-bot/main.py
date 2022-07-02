import time

import selenium
from selenium.webdriver.common.keys import Keys

PROMISED_DOWNLOAD = 300
PROMISED_UP = 300

# Enter twitter email and password
EMAIL =''
PASSWORD=''

CHROME_DRIVER_PATH = 'C:\Program Files\chromedriver_win32\chromedriver.exe'

class InternetSpeedTwitterBot():
    def __init__(self):
        self.up = PROMISED_UP
        self.down = PROMISED_DOWNLOAD
        self.driver = selenium.webdriver.Chrome(CHROME_DRIVER_PATH)
        MESSAGE = f'''HEY prov, why is my internet speed {self.up}up/{self.down}down when i pay for {PROMISED_UP}up/{PROMISED_DOWNLOAD}down?
'''

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/run')
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(45)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)


    def tweet_at_provider(self):
        MESSAGE = f'''HEY prov, why is my internet speed {self.down}down/{self.up}up when i pay for {PROMISED_DOWNLOAD}down/{PROMISED_UP}up?
        '''
        self.driver.get('https://twitter.com/home?lang=en')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(EMAIL)
        time.sleep(2)
        psswrd = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        psswrd.send_keys(PASSWORD)
        psswrd.send_keys(Keys.ENTER)

        time.sleep(10)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(MESSAGE)

        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

        self.driver.quit()

tweeter = InternetSpeedTwitterBot()
tweeter.get_internet_speed()
if tweeter.down <PROMISED_DOWNLOAD or PROMISED_UP > tweeter.up:
    tweeter.tweet_at_provider()