





class Person:
    def __init__(self, first, last, phone):
        self.__first = first
        self.__last = last
        self.__phone = phone

    # Setters
    def set_first(self, name):
        self.__first = name

    def set_last(self, last):
        self.__last = last

    def set_phone(self, phone):
        self.__phone = phone

    # Getters
    def get_first(self):
        return self.__first

    def get_last(self):
        return self.__last

    def get_phone(self):
        return self.__phone

    def __repr__(self):
        return f'{self.__first:<20}{self.__last:<20}{self.__phone:<20}'


class Customer(Person):
    def __init__(self, first, last, phone, email, state, address):
        super().__init__(first, last, phone)
        self.__email = email
        self.__state = state
        self.__address = address

    # Setters
    def set_email(self, email):
        self.__email = email

    def set_address(self, address):
        self.__address = address

    def set_state(self, state):
        self.__state = state

    # Getters
    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_state(self):
        return self.__state

    def __repr__(self):
        return f'{super().__repr__()} {self.__email:<20}{self.__address:<30}{self.__state:<10}'
