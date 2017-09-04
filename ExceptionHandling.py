from selenium import webdriver
from datetime import datetime
import unittest

class SeleniumException(unittest.TestCase):
    # driver = webdriver.Chrome()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="https://www.google.co.in/"
        # base_url = self.base_url
        self.verificationErrors=[]


    def test_ExceptionHandling(self):
        driver = self.driver
        driver.get(self.base_url+ '/')
        # driver.get("https://booking.com")
        driver.maximize_window()
        try:
            driver.find_element_by_id(self,'.//dadad').click();

        except Exception as e:
            print(e)
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            driver.get_screenshot_as_file('Reports\\screenshot-%s.png'%now)
            #driver.get_screenshot_as_file('D://screenshot-%s.png'%now)
            # self.assertEqual([],self.verificationErrors)


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()