
from sys import maxsize


class Contact:

    def __init__(self, name=None, lastname=None, address=None, homephone=None, mobile=None,
                 workphone=None, secondaryphone = None, email=None, secondemail=None, thirdemail=None,
                 id=None, all_phones_from_home_page = None, all_emails_from_home_page=None, full_name_from_home_page=None):
        self.name = name
        self.lastname = lastname
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address = address
        self.secondemail = secondemail
        self.thirdemail = thirdemail
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s; %s; %s; %s; %s; %s; %s; %s; %s; %s" % (self.id, self.name, self.lastname, self.address,
                                                              self.email, self.secondemail, self.thirdemail,
                                                              self.homephone, self.mobile,
                                                              self.workphone, self.secondaryphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.name == other.name and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
