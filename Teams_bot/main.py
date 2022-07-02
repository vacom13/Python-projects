import time
import datetime
import selenium
from selenium.webdriver.common.keys import Keys

# Add your credentials
EMAIL = ''
PASSWORD = ''


# CREATES TIME OBJECT, TO BE USED FOR TIME COMPARISON

def time_rn():
    time_rn = datetime.datetime.now()
    return datetime.datetime(year=1900, month=1, day=1, hour=time_rn.hour, minute=time_rn.minute)




chrome_driver_path = 'C:\chromedriver_win32\chromedriver.exe'

chrome_driver = selenium.webdriver.Chrome(executable_path=chrome_driver_path)





# LOGIN

chrome_driver.get(
    'https://go.microsoft.com/fwlink/p/?LinkID=873020&clcid=0x4009&culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn')

time.sleep(5)

input_email = chrome_driver.find_element_by_id('i0116')
input_email.send_keys(EMAIL)

time.sleep(2)

input_email.send_keys(Keys.ENTER)

time.sleep(5)

input_password = chrome_driver.find_element_by_id('i0118')
input_password.send_keys(PASSWORD)

time.sleep(2)

input_password.send_keys(Keys.ENTER)

time.sleep(5)

chrome_driver.find_element_by_id('idBtn_Back').click()



time.sleep(40)

# POPUP DETECTION


try:
    chrome_driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/div[1]/div[2]/button').click()
    time.sleep(5)
except:
    pass

try:
    chrome_driver.find_element_by_xpath('//*[@id="engagement-surface-dialog"]/div/div/div[1]/div/button').click()
    time.sleep(5)
except:
    pass

try:
    chrome_driver.find_element_by_xpath('//*[@id="engagement-surface-dialog"]/div/div/div[3]/div/div').click()
    time.sleep(5)
except:
    pass

# CALENDER OPENING

chrome_driver.find_element_by_id('app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c').click()

time.sleep(5)

day = chrome_driver.find_element_by_id('id__16')
day.click()

time.sleep(5)

chrome_driver.find_element_by_xpath('//*[@id="id__16-menu"]/div/ul/li[1]/button/div').click()

time.sleep(5)

# GETTING THE NUMBER OF CLASSES AS A LIST

list_of_classes = chrome_driver.find_elements_by_class_name(
    'node_modules--msteams-bridges-components-calendar-grid-dist-es-src-renderers-calendar-multi-day-renderer-calendar-multi-day-renderer__eventCard--3NBeS')
counter = 0
number_of_classes = len(list_of_classes)
number_of_classes_attended = 0

while (counter < number_of_classes):

    # LOOKING FOR THE CLASS

    list_of_classes = chrome_driver.find_elements_by_class_name(
        'node_modules--msteams-bridges-components-calendar-grid-dist-es-src-renderers-calendar-multi-day-renderer-calendar-multi-day-renderer__eventCard--3NBeS')
    i = list_of_classes[counter]
    i.click()

    # GETTING THE TIME OF THE CLASS

    datetime_str = chrome_driver.find_element_by_class_name(
        'node_modules--msteams-bridges-components-calendar-grid-dist-es-src-renderers-peek-renderer-peek-meeting-header-peek-meeting-header__date--3K2O_').text[
                   12:]
    timings = datetime_str.split('-')


    start_time = datetime.datetime.strptime(timings[0].lstrip().rstrip(), '%I:%M %p')
    end_time = datetime.datetime.strptime(timings[1].lstrip().rstrip(), '%I:%M %p')
    current_time = time_rn()

    time.sleep(5)

    # IF THE SELECTED CLASS MATCHES CURRENT TIME, JOIN ELSE GO TO THE NEXT CLASS

    if (current_time > end_time):
        pass

        chrome_driver.find_element_by_xpath('//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]').click()
        counter += 1
    else:
        # IF THE TIME IS BEFORE THE START TIME, WAIT TILL 5 MINS REMAIN TO JOIN
        if (start_time - current_time).total_seconds() > 300:
            time.sleep((start_time - current_time).total_seconds() - 300)

        # print(timings)
        chrome_driver.find_element_by_xpath(
            '/html/body/div[9]/div/div/div/div[3]/div/div/div[1]/div[2]/div[3]/button[1]').click()

        time.sleep(35)

        chrome_driver.find_element_by_xpath(
            f'//*[@id="ngdialog{number_of_classes_attended + 1}"]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()

        time.sleep(5)

        chrome_driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div').click()
        current_time = time_rn()
        time.sleep((end_time - current_time).total_seconds())

        chrome_driver.find_element_by_xpath('//*[@id="app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"]').click()

        time.sleep((time_rn()-end_time).total_seconds())

        chrome_driver.find_element_by_xpath('//*[@id="hangup-button"]').click()
        counter += 1
        number_of_classes_attended += 1
        time.sleep(10)
