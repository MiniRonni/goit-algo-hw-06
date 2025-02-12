from collections import UserDict


class Field:
    """Base class for record fields."""
    def __init__(self, value):
        """Initializing a field with a value."""
        self.value = value


    def __str__(self):
        """Returns a string representation of the field value."""
        return str(self.value)


class Name(Field):
    """Class for storing contact name."""
    def __init__(self, value):
        """Check for empty name."""
        if not value:
            raise ValueError('Name cannot be empty.')
        super().__init__(value)


class Phone(Field):
    """Class for storing phone numbers."""
    def __init__(self, value):
        """Checking the phone number is correct."""
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Phone is required')
        super().__init__(value)


class Record:
    """Class for storing contact information"""
    def __init__(self, name):
        """Initialize a record with a name and an empty list of phones."""
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        """Adds a new phone to the contact list."""
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        """Deletes a phone number from contacts."""
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError('Phone not found')


    def edit_phone(self, old_phone, new_phone):
        """Edits the phone number for a contact."""
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            phone_obj.value = new_phone
        else:
            raise ValueError('Old phone not found')


    def find_phone(self, phone):
        """Searches for a phone in the list by number."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None


    def __str__(self):
        """Returns a string representation of a contact with phones."""
        return f"Contact name: {self.name.value}, phone: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Class for storing and managing records."""
    def add_record(self, record):
        """Adds a new entry to the address book."""
        self.data[record.name.value] = record


    def find(self, name):
        """Searches for a record by name."""
        return self.data.get(name)


    def delete(self, name):
        """Deletes an entry by name."""
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError('Contact not found')


    def __str__(self):
        """Returns a string representation of the entire address book."""
        return "\n".join(str(record) for record in self.data.values())
    

# Test case
book = AddressBook()

# Adding contacts
john_rec = Record("John")
john_rec.add_phone("1234567890")
john_rec.add_phone("9876543210")
book.add_record(john_rec)

jane_rec = Record("Jane")
jane_rec.add_phone("5555555555")
jane_rec.add_phone("9999999999")
book.add_record(jane_rec)

print(book) # Display the entire address book

# Change John's phone number
john = book.find("John")
john.edit_phone("1234567890", "6543210987")
print(john)

# Looking for John's phone number
found_phone = john.find_phone("6543210987")
print(f"{john.name}: {found_phone}")

print(book) # Output the updated address book

# Delete contact Jane
book.delete("Jane")
print(book)