class Student:
    def __init__(self, album_number, first_name, last_name, city, street, zip_code):
        self.album_number = album_number
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return (
            f"Student: {self.album_number} {self.first_name} {self.last_name}, "
            f"Address: {self.city} {self.street}, {self.zip_code}"
        )
