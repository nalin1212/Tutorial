

# example of encapsulation in Python
class user:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    def clean_email(self):
         return self.__email.lower().strip()     
    # (__email ) can be accessed only within the class, not outside of it. This is an example of encapsulation.
    # It makes the email attribute private and prevents it from being accessed or modified directly from outside the class.

    def say_hi_to_user(self, user):
        print(f"sending message to {user.username}: Hi {user.username}, it's {self.username} here")




user1 = user("Don", "Don@example.com",("123-456-7890"))
user2 = user("Alice", "alice@example.com",("098-765-4321"))
user1.say_hi_to_user(user2)

print(user1.clean_email())
print(user1.__email) # This will raise an AttributeError because __email is a private attribute and cannot be accessed directly from outside the class.


