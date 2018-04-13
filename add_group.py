# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

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
        wd = self.wd
        # Open homepage
        wd.get("http://localhost/addressbook/group.php")
        # Login
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        # Open groups page
        wd.find_element_by_link_text("groups").click()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").send_keys("New group 1")
        wd.find_element_by_name("group_header").send_keys("Group header 1")
        wd.find_element_by_name("group_footer").send_keys("Group footer")
        # Submit group creation
        wd.find_element_by_name("submit").click()
        # Return to group page
        wd.find_element_by_link_text("groups").click()
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()