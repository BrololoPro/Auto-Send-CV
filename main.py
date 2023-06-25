import undetected_chromedriver as webdriver
from selenium.webdriver.common.keys import Keys
import os

#Overcharge the method so that the webbrowser doesn't close when it finished it'ss task
class MyUDC(webdriver.Chrome):
    def __del__(self):
        try:
            self.service.process.kill()
        except:  # noqa
            pass
        # self.quit()

#Rewrite type element.clear() definitely not working on chrome
def clear_texte(element):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE) 

username = os.getlogin()

#Load Chrome's first profile to automatically log in the apps
options= webdriver.ChromeOptions()
profile = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")

#Start the web browser with the recquired options
browser = MyUDC(options=options, use_subprocess=True)

#Open the webside
browser.get("https://fr.indeed.com/")

whatInput = browser.find_element("id", "text-input-what")
clear_texte(whatInput)
whatInput.send_keys("Développeur python")

whereInput = browser.find_element("id", "text-input-where")
clear_texte(whereInput)
whereInput.send_keys('Bordeaux')

searchButton = browser.find_element("class name", "yosegi-InlineWhatWhere-primaryButton").click()

# html = browser.page_source

# print(html)