
class Contact:

    def __init__(self, name=None, mobile=None, email=None, id=None):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name