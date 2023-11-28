class Contact:    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __iter__(self):
        yield self.name
        yield self.phone

class Birthday: 
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __iter__(self):
        yield self.name
        yield self.birthday   