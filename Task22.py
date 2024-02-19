from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class GuviInstaPage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def quit(self):
        self.driver.quit()

    def getNumberofPost(self):
        xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button/span/span"   
        posts = self.driver.find_element(by=By.XPATH, value=xpath).text
        return posts
    

url = "https://www.instagram.com/guviofficial/"      
obj = GuviInstaPage(url)
obj.boot()
print(obj.getNumberofPost())
obj.quit()  