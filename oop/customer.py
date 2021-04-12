


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
        
cu = Customer('Peter', 99998888)

print(cu)