import shelve


#donation
class Donor:
    def __init__(self, item, quantity, expiry, req, email):
        self.__id = email + ":" + item
        self.__item = item
        self.__quantity = quantity
        self.__expiry = expiry
        self.__req = req
        self.__email = email

    def set_item(self, item):
        self.__item = item

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_expiry(self, expiry):
        self.__expiry = expiry

    def set_req(self, req):
        self.__req = req

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_item(self):
        return self.__item

    def get_quantity(self):
        return self.__quantity

    def get_expiry(self):
        return self.__expiry

    def get_req(self):
        return self.__req


donors = shelve.open('Donor')
users = shelve.open('Users')
admin = shelve.open('Admin')

def create_donor(donor):
     donors[donor.get_id()] = donor

def update_donor(donor):
    donors[donor.id] = donor


def delete_donors(id):
    if id in donors:
        del donors[id]

def get_donors():
    keys = list(donors.keys())
    x = []
    for i in keys:
        x.append(donors.get(i))
    return x
def get_donor(id):
    if id in donors:
        return donors[id]


def delete_donors(id):
    if id in donors:
        del donors[id]

#admindonor
class Admindonor:
    def __init__(self, donor, item, quantity, expiry, req, email):
        self.__donor = donor
        self.__id = email + ":" + item
        self.__item = item
        self.__quantity = quantity
        self.__expiry = expiry
        self.__req = req
        self.__email = email

    def set_item(self, item):
        self.__item = item

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_expiry(self, expiry):
        self.__expiry = expiry

    def set_req(self, req):
        self.__req = req

    def get_email(self):
        return self.__email

    def get_donor(self):
        return self.__donor

    def set_donor(self):
        self.__donor = donor


    def set_email(self, email):
        self.__email = email

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_item(self):
        return self.__item

    def get_quantity(self):
        return self.__quantity

    def get_expiry(self):
        return self.__expiry

    def get_req(self):
        return self.__req


#userprofile

class user:
    def __init__(self, name, email1, address, people):
        self.__name = name
        self.__email1 = email1
        self.__address = address
        self.__people = people

    def set_name(self, name):
        self.__name = name

    def set_email1(self, email1):
        self.__email1 = email1

    def set_address(self, address):
        self.__address = address

    def set_people(self, people):
        self.__people = people

    def get_name(self):
        return self.__name

    def get_email1(self):
        return self.__email1

    def get_address(self):
        return self.__address

    def get_people(self):
        return self.__people

def get_user(id):
    return users[id]

def update_user(user):
    users[user.get_email1()] = user



