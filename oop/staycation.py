


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
    
h1 = Staycation('Grand Marina', 2, 199)
h2 = Staycation('random', 1, 49)

print(h1.isCheaper(h2))
print(h1)
h1.voucherAllowed(False)
print(h1)