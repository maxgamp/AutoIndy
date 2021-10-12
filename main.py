from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


def setSubject(hour):
    hour.click()
    
    selectVal = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//option[contains(text(), 'L12')]")))[0]
    
    teacherbox = Select(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "Lehrerbox")))[0])
    teacherbox.select_by_visible_text(selectVal.text)

    activitybox = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "Activity")))[0]
    activitybox.clear()
    activitybox.send_keys("Mathematik üben")

    submit = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "saveModalSaveButton")))[0]
    submit.click()

with open(".\\login.txt", 'r') as f:
    username = f.readline()
    passwd = f.readline()

driver = webdriver.Firefox()

driver.implicitly_wait(5)

driver.get("https://indy.sz-ybbs.ac.at/pages/loginLogout/login.php")

username_box = driver.find_element_by_id("loginWidget.idusername")

password_box = driver.find_element_by_id("loginWidget.idpassword")

username_box.send_keys(username)
password_box.send_keys(passwd)
password_box.send_keys(Keys.RETURN)

nextBtn = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pull-right")))[0]
prevBtn = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pull-right")))[0]

try:
    testxpath = driver.find_elements_by_xpath("//div[contains(@class, 'CalendarToDoNotEnoughEntriesRegistered')]")
    
    print(f"XpathLen: {len(testxpath)}")

    for item in testxpath:
        print(item.get_attribute('class'))
except:
    print("Something went wrong with xpath")

alldays = driver.find_elements_by_xpath("//div[contains(@class, 'CalendarToDoNotEnoughEntriesRegistered')]")

time.sleep(2)

for day in alldays:
    item.click()
    hour0 = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "Stunde0")))[0]
    setSubject(hour0)
    
    time.sleep(1)

    item.click()
    hour1 = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.ID, "Stunde1")))[0]
    setSubject(hour1)

    time.sleep(1)