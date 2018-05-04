from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        # Click "Add new" - going to creation form
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # Click Enter (create a contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # Fill in general information
        self.change_text_field_value("firstname", contact.first_name)
        self.change_text_field_value("middlename", contact.middle_name)
        self.change_text_field_value("lastname", contact.last_name)
        self.change_text_field_value("nickname", contact.nickname)
        self.change_text_field_value("title", contact.title)
        self.change_text_field_value("company", contact.company)
        self.change_text_field_value("address", contact.address)
        # Fill in telephones information
        self.change_text_field_value("home", contact.home_phone)
        self.change_text_field_value("mobile", contact.mobile_phone)
        self.change_text_field_value("work", contact.work_phone)
        self.change_text_field_value("fax", contact.fax)
        # Fill in emails and other
        self.change_text_field_value("email", contact.email1)
        self.change_text_field_value("email2", contact.email2)
        self.change_text_field_value("email3", contact.email3)
        self.change_text_field_value("homepage", contact.homepage_link)
        self.change_select_list_value(contact.birthday_day)
        self.change_select_list_value(contact.birthday_month)
        self.change_text_field_value("byear", contact.birthday_year)
        self.change_select_list_value(contact.anniversary_day)
        self.change_select_list_value(contact.anniversary_month)
        self.change_text_field_value("ayear", contact.anniversary_year)
        # Fill in secondary information
        self.change_text_field_value("address2", contact.secondary_address)
        self.change_text_field_value("phone2", contact.home_phone2)
        self.change_text_field_value("notes", contact.notes)

    def change_text_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_list_value(self, select_list):
        wd = self.app.wd
        if select_list is not None:
            wd.find_element_by_xpath(select_list).click()

    def edit_first(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # click "edit"
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # Click Enter (create a contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                l_name = element.find_element_by_xpath(".//td[2]").text
                f_name = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(last_name = l_name, first_name = f_name, id = id))
        return list(self.contact_cache)