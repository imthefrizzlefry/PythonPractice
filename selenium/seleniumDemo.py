import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
import time
import logging

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):

        logging.basicConfig(level=logging.DEBUG)
        # set Chrome options to create a headless chrome session
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        # create a new Chrome session
        inst.driver = webdriver.Chrome(chrome_options=chrome_options)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()    

    # @classmethod
    # def tearDown(inst):
    #     inst.driver.delete_all_cookies()

    def test_search_by_text(inst):
        
        # navigate to the application home page
        inst.driver.get("http://www.google.com/")

        # get the search textbox
        search_field = inst.driver.find_element_by_name("q")

        # enter search keyword and submit
        search_field.send_keys("Selenium WebDriver Interview questions")
        search_field.submit()

        

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod
        lists = inst.driver.find_elements_by_class_name("r")
        no=len(lists)
        logging.debug("{0}: ************************************************************************    number of ItemsInList: {1}".format("test_search_by_text", no))
        #time.sleep(2)

        inst.assertEqual(14, no)

    def test_search_python(inst):
        inst.driver.get("http://python.org")

        elem = inst.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        logging.debug("{0}: ************************************************************************    results are being displayed".format("test_search_python"))
        #time.sleep(2)

    def test_zestimateForMyHouse(inst):
        inst.driver.get(r"https://www.zillow.com//homedetails/8921-NE-142nd-St-Kirkland-WA-98034/48881717_zpid/?utm_source=email&utm_medium=email&utm_campaign=emo-sendtofriend-hdp&rtoken=045f7371-c3bf-4437-a2a1-187160392747~X1-ZUy4fq4ggnsirt_2ox8a")
     
        pageTitle = inst.driver.title

        if pageTitle:
            logging.debug("{0}: ************************************************************************    The Current Page Title is: \"{1}\"".format("test_getZestimateForMyHouse", pageTitle))
            
            elem = inst.driver.find_element_by_class_name("zestimate")
            zestimate = elem.text.split(' ')[1]
            logging.debug("{0}: ************************************************************************    Zestimate Is: {1}".format("test_getZestimateForMyHouse", zestimate))
        else:
            logging.debug("{0}: ************************************************************************    Stupid Captcha!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".format("test_getZestimateForMyHouse"))

if __name__ == '__main__':
    unittest.main()