from model.contact import Contact
import getopt
import sys
import jsonpickle
import os.path
import random
import string


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols).strip() for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.ascii_letters + string.digits*20 + "+" + "(" + ")" + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_date(maxlen):
    return random.randint(0, maxlen)


testdata = [
    Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="", home_phone="",
            mobile_phone="", work_phone="", fax="", email1="", email2="", email3="", homepage_link="", birthday_year="",
            anniversary_year="", secondary_address="", home_phone2="", notes="")] + [
    Contact(first_name=random_string("fname", 10), middle_name=random_string("mname", 10), last_name=random_string("lname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 10),
            address=random_string("address", 50), home_phone=random_phone(20), mobile_phone=random_phone(20),
            work_phone=random_phone(20), fax=random_phone(20), email1=random_string("email1", 20),
            email2=random_string("email2", 20), email3=random_string("email3", 20), homepage_link=random_string("hp_link", 40),
            birthday_day=random_date(32), birthday_month=random_date(12), birthday_year=random_string("", 10),
            anniversary_day=random_date(32), anniversary_month=random_date(12), anniversary_year=random_string("", 10),
            secondary_address=random_string("address2", 50), home_phone2=random_phone(20), notes=random_string("notes", 50))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))