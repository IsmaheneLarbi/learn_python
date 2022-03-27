import datetime

class User:
    pass

user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name, user1.last_name)

first_name = "Arthur"
last_name = "Clarke"

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"
print(user2.first_name, user2.last_name)
user1.age = 35
user2.favorite_book = "2001: A Space Odyssey"
# print(user2.age) throws attribute error

class User:
    def __init__(self, full_name, birthday):
        """A member of our social medium.
        A member has a full_name, first_name, last_name and a birthday"""
        self.name = full_name
        self.birthday = birthday 

        # Extract first and last names:
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]

    def age(self):
        """Returns the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob) / 365
        return int(age_in_years)

user = User("Dave Bowman", "19710315")
print(help(User))
