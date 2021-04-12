
from oop.customer import Customer


class Booking:
    
    def __init__(self, _customer: Customer, _staycation, _checkInDate, cost):
        self._customer = _customer
        self._staycation = _staycation
        self._checkInDate = _checkInDate
        self.cost = cost
      
    def get_name(self):
        return self._name

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

