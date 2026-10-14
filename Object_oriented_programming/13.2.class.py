
from datetime import datetime

# example of encapsulation in Python
class user:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password  
    def get_email(self):
        print(f"Email acessed at{datetime.now()}")
        return self._email
    def set_email(self,new_email):
        if "@" in new_email:
            self._email = new_email

             

    # def say_hi_to_user(self, user):
        # print(f"sending message to {user.username}: Hi {user.username}, it's {self.username} here")




user1 = user("Don", "Don@example.com",("123-456-7890"))
print(user1.get_email())
# user2 = user("Alice", "alice@example.com",("098-765-4321"))
# user1.say_hi_to_user(user2)

# print(user1.get_email())
user1.set_email("danny@outlook.com")
print(user1.get_email()) # This will raise an AttributeError because __email is a private attribute and cannot be accessed directly from outside the class.


