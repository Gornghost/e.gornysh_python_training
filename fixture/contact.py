from model.contact import Contact
import re


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
        self.date_day("bday", contact.birthday_day)
        self.change_select_list_value(contact.birthday_month)
        self.change_text_field_value("byear", contact.birthday_year)
        self.change_select_list_value(contact.anniversary_day)
        self.change_select_list_value(contact.anniversary_month)
        self.change_text_field_value("ayear", contact.anniversary_year)
        # Fill in secondary information
        self.change_text_field_value("address2", contact.secondary_address)
        self.change_text_field_value("phone2", contact.home_phone2)
        self.change_text_field_value("notes", contact.notes)

    def date_day(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            select_list = wd.find_element_by_name(field_name)
            select_list.find_elements_by_tag_name("option")[value].click()

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
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.open_edit_page_by_index(index)
        self.fill_contact_form(new_contact_data)
        # Click Enter (create a contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_edit_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        contact = wd.find_elements_by_name("entry")[index]
        contact.find_element_by_xpath(".//td[8]/a/img").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        contact = wd.find_elements_by_name("entry")[index]
        contact.find_element_by_xpath(".//td[7]/a/img").click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
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
                cells = element.find_elements_by_tag_name("td")
                l_name = cells[1].text
                f_name = cells[2].text
                address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(last_name=l_name, first_name=f_name, address=address, id=id,
                                                  all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_page_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        homephone2 = wd.find_element_by_name("phone2").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(last_name=lastname, first_name=firstname, address=address, email1=email, email2=email2,
                       email3=email3, home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone,
                       home_phone2=homephone2, id=id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        homephone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone, home_phone2=homephone2)