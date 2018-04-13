# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys("New group 1")
        wd.find_element_by_name("group_header").send_keys("Group header 1")
        wd.find_element_by_name("group_footer").send_keys("Group footer")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()