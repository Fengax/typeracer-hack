from selenium import webdriver
import time
import random

from selenium.common.exceptions import ElementNotInteractableException

username_input = input("Username: ")
password_input = input("Password: ")

browser = webdriver.Chrome("chromedriver")
browser.get("https://play.typeracer.com/")
wrong_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", ",", ".", ";", ":"]

time.sleep(5)

login_button = browser.find_element_by_css_selector("#tstats > table > tbody > tr.datarow > td:nth-child(1) > table > tbody > tr > td:nth-child(1) > a")
login_button.click()
username_field = browser.find_element_by_css_selector("body > div.DialogBox.trPopupDialog.editUserPopup > div > div > div.dialogContent > div > div.bodyWidgetHolder > div > table.gwt-DisclosurePanel.gwt-DisclosurePanel-open > tbody > tr:nth-child(2) > td > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > input")
username_field.send_keys(username_input)
password_field = browser.find_element_by_css_selector("body > div.DialogBox.trPopupDialog.editUserPopup > div > div > div.dialogContent > div > div.bodyWidgetHolder > div > table.gwt-DisclosurePanel.gwt-DisclosurePanel-open > tbody > tr:nth-child(2) > td > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > input")
password_field.send_keys(password_input)
submit_button = browser.find_element_by_css_selector("body > div.DialogBox.trPopupDialog.editUserPopup > div > div > div.dialogContent > div > div.bodyWidgetHolder > div > table.gwt-DisclosurePanel.gwt-DisclosurePanel-open > tbody > tr:nth-child(2) > td > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > table > tbody > tr > td:nth-child(1) > button")
submit_button.click()

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
        except:
            break

    input_box = browser.find_element_by_class_name("txtInput")

    for i in text:
        rand_wrong_key = random.randint(rand_lower_bound, rand_upper_bound)
        if  rand_wrong_key == 5:
            try:
                input_box.send_keys(wrong_keys[random.randint(0, 31)])
                time.sleep(random.randint(20, 60) * 0.001)
                input_box.send_keys('\b')
                time.sleep(random.randint(20, 60) * 0.001)
                input_box.send_keys(i)
                time.sleep(random.randint(20, 60) * 0.001)
            except ElementNotInteractableException:
                pass
        else:
            try:
                input_box.send_keys(i)
                time.sleep(random.randint(20, 60) * 0.001)
            except ElementNotInteractableException:
                pass

    again = input("Race again? Yes/No")

    if again == "Yes":
        race_again = browser.find_element_by_class_name("raceAgainLink")
        race_again.click()
        time.sleep(2)
    elif again == "No":
        break