from collections import UserDict


# Базовий клас для полів запису.
class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


# Клас для зберігання імені контакту
class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError('Name cannot be empty.')
        super().__init__(value)


# Клас для зберігання номера телефону.
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Phone is required')
        super().__init__(value)


# Клас для зберігання інформації про контакт
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError('Phone not found')


    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = new_phone
        else:
            raise ValueError('Old phone not found')


    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


    def __str__(self):
        return f"Contact name: {self.name.value}, phone: {'; '.join(p.value for p in self.phones)}"


# Клас для зберігання та управління записами.
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data.get(name)


    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError('Contact not found')


    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    

# Виконання
book = AddressBook()

john_rec = Record("John")
john_rec.add_phone("1234567890")
john_rec.add_phone("9876543210")

book.add_record(john_rec)

jane_rec = Record("Jane")
jane_rec.add_phone("5555555555")
jane_rec.add_phone("9999999999")

book.add_record(jane_rec)

print(book)

john = book.find("John")
john.edit_phone("1234567890", "6543210987")

print(john)

found_phone = john.find_phone("6543210987")

print(f"{john.name}: {found_phone}")

print(book)

book.delete("Jane")
print(book)