from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
import threading

def wpm_to_delay(wpm):
    ratio = wpm/105
    delay = 0.001/ratio
    return delay

username_input = input("Username: ")
password_input = input("Password: ")
delay = wpm_to_delay(int(input("Target WPM: ")))

ua = UserAgent()
userAgent = ua.random
options = webdriver.ChromeOptions()
#options.add_argument('user-agent={userAgent}')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options, executable_path=r'D:\typeracer-hack\chromedriver.exe')
browser.get("https://play.typeracer.com/")
wrong_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ",", ".", ";", ":"]

time.sleep(2)
'''
while True:
    try:
        login_button = browser.find_element_by_css_selector("#tstats > table > tbody > tr.datarow > td:nth-child(1) > table > tbody > tr > td:nth-child(1) > a")
        login_button.click()
        break
    except:
        pass
time.sleep(1)
username_field = browser.find_element_by_class_name("gwt-TextBox")
username_field.click()
for i in username_input:
    username_field.send_keys(i)
    time.sleep(random.randint(10, 50) * delay)
time.sleep(1)
password_field = browser.find_element_by_class_name("gwt-PasswordTextBox")
password_field.click()
for i in password_input:
    password_field.send_keys(i)
    time.sleep(random.randint(10, 50) * delay)
time.sleep(1)
submit_button = browser.find_element_by_class_name("gwt-Button")
submit_button.click()

time.sleep(3)
'''
race_button = browser.find_element_by_css_selector("#dUI > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.mainViewport > div > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > a")
race_button.click()

time.sleep(1)

while True:
    rand_lower_bound = random.randint(0, 3)
    rand_upper_bound = random.randint(12, 15)

    content = browser.find_element_by_class_name('inputPanel')
    text = content.text

    while True:
        try:
            browser.find_element_by_class_name("countdownPopup")
        except Exception as e:
            break

    time.sleep(0.01)
    input_box = browser.find_element_by_class_name("txtInput")
    
    for i in range(0, len(text) - 10):
        rand_wrong_key = random.randint(rand_lower_bound, rand_upper_bound)
        if rand_wrong_key == 5:
            rand_wrong_key_iter = random.randint(0, 5)
            try:
                for x in range(0, rand_wrong_key_iter):
                    t1 = threading.Thread(target=input_box.send_keys, args=(text[i + x + 1],))
                    t1.start()
                    t1.join()
                    time.sleep(random.randint(10, 50) * delay)
                for z in range(0, rand_wrong_key_iter):
                    t1 = threading.Thread(target=input_box.send_keys, args=('\b',))
                    t1.start()
                    t1.join()
                    time.sleep(random.randint(10, 50) * delay)
                t1 = threading.Thread(target=input_box.send_keys, args=(text[i],))
                t1.start()
                t1.join()
                time.sleep(random.randint(10, 50) * delay)
            except:
                pass
        else:
            try:
                t1 = threading.Thread(target=input_box.send_keys, args=(text[i],))
                t1.start()
                t1.join()
                time.sleep(random.randint(10, 50) * delay)
            except:
                pass

    for i in range(len(text) - 10, len(text) - 1):
        try:
            t1 = threading.Thread(target=input_box.send_keys, args=(text[i],))
            t1.start()
            t1.join()
            time.sleep(random.randint(10, 50) * delay)
        except:
            pass

    time.sleep(3)
    while True:
        try:
            race_again = browser.find_element_by_class_name("raceAgainLink")
            race_again.click()
            break
        except:
            pass
    time.sleep(2)