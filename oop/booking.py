
# from oop.staycation import Staycation
# from oop.customer import Customer
import datetime

class Staycation:
    
    def __init__(self, _hotelName, _nights, _cost):
        self._hotelName = _hotelName
        self._nights = _nights
        self._cost = _cost
        self._voucherAllowed = True
    
    def hotelName(self):
        return self._hotelName

    def nights(self):
        return self._nights
    
    def cost(self):
        return self._cost

    def voucherAllowed(self):
        return self._voucherAllowed

    def cost(self, contact):
        self._contact = contact

    def voucherAllowed(self, voucher):
        self._voucherAllowed = voucher

    def costPerNight(self):
        return self._cost

    def isCheaper(self, other):
        if self._cost < other._cost:
            return True
        return False

    def __str__(self) -> str:
        var = ''
        if self._voucherAllowed:
            var = 'Yes'
        else:
            var = 'No'
        return self._hotelName +' Nights: '+ str(self._nights) + ' Current Price: $'+str(round(self._cost*self._nights, 2))  + " or $"+str(format(self._cost, '.2f'))+ " per night Voucher allowed: "+var

class Customer:
    
    def __init__(self, _name, _contact):
        self._name = _name
        self._contact = _contact
      
    def name(self):
        return self._name

    def contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

    def __str__(self) -> str:
        return self._name + " " + str(self._contact)


class Booking:
    
    def __init__(self, customer: Customer, staycation: Staycation, checkInDate: datetime):
        self._customer = customer
        self._staycation = staycation
        self._checkInDate = checkInDate
        self._cost = staycation._cost
    
    def customer(self):
        return self._customer
    
    def staycation(self):
        return self._staycation

    def hotelName(self):
        return self._staycation._hotelName

    def checkInDate(self):
        return self._checkInDate

    def checkOutDate(self):
        return self._checkInDate + datetime.timedelta(days=self._staycation.nights())

    def cost(self):
        return self._cost
    
    def costDifferenceFromcurrent(self, cost):
        return abs(cost - self._cost)

    def __str__(self) -> str:
        
        return "Booked at: $" + str(self._cost*self._staycation.nights()) + " Check-in Date: " + str(self.checkInDate()) + " Check-out Date: "+ str(self.checkOutDate())
        
cu = Customer('Peter', 99998888)
h1 = Staycation('Grand Marina', 2, 199)
h2 = Staycation('random', 1, 49)

newbook = Booking(cu, h1, datetime.datetime.now())
print(h1)
print(newbook)
print(cu)