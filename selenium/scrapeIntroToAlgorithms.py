from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import logging

class PageDriver:
    def __init__(self, base_url="https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/rss.xml"):
        # set Chrome options to create a headless chrome session
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = "./selenium/drivers/"
        logging.debug(chrome_options.binary_location)

        logging.debug(chrome_options)
        # create a new Chrome session
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = base_url

    def closeBrowser(self):
        self.driver.quit() 

    def getVideoUrls():
        driver.get(self.base_url)
        video_selector = "a[contains(text, 'Internet Archive(MP4)')]"
        logging.debug("selector: {}".format(video_selector))

        logging.debug(div.find_element_by_css_selector('a').get_attribute('href'))






if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    my_page = PageDriver()

