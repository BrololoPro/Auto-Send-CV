import undetected_chromedriver as webdriver

#Overcharge the method so that the webbrowser doesn't close when it finished it'ss task
# class MyUDC(webdriver.Chrome):
#     def __del__(self):
#         try:
#             self.service.process.kill()
#         except:  # noqa
#             pass
#         # self.quit()


#Load Chrome's first profile to automatically log in the apps
options= webdriver.ChromeOptions()
profile = "C:\\Users\\laure\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")

#Start the web browser with the recquired options
browser = webdriver.Chrome(options=options, use_subprocess=True)

#Open the webside
browser.get("https://fr.indeed.com/")

inputElement = browser.find_element_by_id("text-input-what")
inputElement.send_keys('1')


# html = browser.page_source

# print(html)