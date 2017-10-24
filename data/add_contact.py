
from model.contact import Contact
import random
import string


constant = [
    Contact(name="name1", lastname="lastname1", email="email123@gmail.com", address="address1", mobile="111", homephone="333"),
    Contact(name="name2", lastname="lastname2", email="email22@gmail.com", address="address2", mobile="222", homephone="444")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", lastname="", email="", address="", mobile="", homephone="")] + [
    Contact(name=random_string("name", 10), lastname=random_string("lastname", 10), address=random_string("address", 15),
            mobile=random_string("159", 10), homephone=random_string("3578", 5))
    for i in range(1)
]