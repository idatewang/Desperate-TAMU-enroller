from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import random
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# automates headless Chrome brower
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cas.tamu.edu/cas/login?service=https://howdy.tamu.edu/uPortal/Login&renew=true")

username = driver.find_element_by_xpath(xpath="//*[@id=\"username\"]")
username.send_keys("Put Username here")

password = driver.find_element_by_xpath(xpath="//*[@id=\"password\"]")
password.send_keys("Put Password here")

button = driver.find_element_by_xpath(xpath="//*[@id=\"fm1\"]/button")
button.click()

driver.switch_to.frame("duo_iframe")

duo = driver.find_element_by_xpath(xpath="//*[@id=\"auth_methods\"]/fieldset/div[1]/button")
duo.click()

while True:
    try:
        Registration = driver.find_element_by_xpath(xpath="//*[@id=\"tamu-registration-icon-ban9\"]")
        Registration.click()
        break
    except NoSuchElementException:
        continue

time.sleep(2)
register = driver.find_element_by_xpath(xpath="//*[@id=\"registerLink\"]/span[1]")
register.click()

term = driver.find_element_by_xpath(xpath="//*[@id=\"s2id_txt_term\"]/a")
term.click()
time.sleep(2)
term = driver.find_element_by_xpath(xpath="//*[@id=\"202031\"]") # for Spring 2020
term.click()

cont = driver.find_element_by_xpath(xpath="//*[@id=\"term-go\"]")
cont.click()

time.sleep(2)

# selects CESE class
subject = driver.find_element_by_xpath(xpath="//*[@id=\"s2id_txt_subject\"]")
subject.click()
time.sleep(3)
subject = driver.find_element_by_xpath(xpath="//*[@id=\"s2id_autogen5\"]")
subject.send_keys("CSCE")
time.sleep(3)
subject = driver.find_element_by_xpath(xpath="//*[@id=\"CSCE\"]")
subject.click()

# selects course number i.e. 411
number = driver.find_element_by_xpath(xpath="//*[@id=\"txt_courseNumber\"]")
number.send_keys("411")

while True:
    search = driver.find_element_by_xpath(xpath="//*[@id=\"search-go\"]")
    search.click()

    time.sleep(5)
    remain = driver.find_element_by_xpath(xpath="//*[@id=\"table1\"]/tbody/tr[2]/td[11]/span[3]/span[2]")
    
    # prints remaining seats
    print("Remaining:", remain.text)

    if int(remain.text) != 0:
        add = driver.find_element_by_xpath(xpath="//*[@id=\"addSection20203131260\"]")
        add.click()
        sub = driver.find_element_by_xpath(xpath="//*[@id=\"saveButton\"]")
        break
    elif int(remain.text) == 0:
        again = driver.find_element_by_xpath(xpath="// *[ @ id = \"search-again-button\"]")
        again.click()
    ran = random.randint(1, 3)
    time.sleep(ran)
