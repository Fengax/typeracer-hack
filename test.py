from selenium import webdriver
from fake_useragent import UserAgent

ua = UserAgent()
userAgent = ua.random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={userAgent}')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options, executable_path=r'D:\typeracer-hack\chromedriver.exe')
browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")