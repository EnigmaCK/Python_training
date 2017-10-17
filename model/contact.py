
from sys import maxsize


class Contact:

    def __init__(self, name=None, lastname=None, homephone=None, mobile=None,
                 workphone=None, secondaryphone = None, email=None, id=None):
        self.name = name
        self.lastname = lastname
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.name == other.name and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
