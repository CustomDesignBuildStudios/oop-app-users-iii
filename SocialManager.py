# Import and create your users here
import datetime 
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from Post import Post
from User import User

class SocialManager():
    def __init__(self):
        self.current_user = None
        self.users=[]
        pass

    def add_user(self,user):
        self.users.append(user)
        return user

    def display_all_posts(self, order = "ASC"):
        all_posts = []
        for user in self.users:
            all_posts.extend(user.get_posts)
        
        all_posts = sorted(all_posts, key=lambda obj: obj._id)

        print(f"Timeline: {self.get_post_count()} Posts")
        if order == "DSC":
            all_posts = reversed(all_posts)

        for post in all_posts:
            print(post)          
            
    def get_post_count(self):
        count = 0
        for user in self.users:
            count += len(user.get_posts)

        return count
    

    def signup(self, name, age, username, password):
        for user in self.users:
            if user.get_username == username:
                return (False, f"Username already exits", None)
          
        user = User(name, age, username, password)
        self.add_user(user)
        return (True, "User created", user)
    
    def signin(self, username, password):
        for user in self.users:
            if user.get_username == username and user.get_password == password:
                return (True, f"Sign in as {user.get_name}", user)
          
        return (False, "Invalid Password or Username", None)

    def set_current_user(self, user):
        self.current_user = user
        

    def display_menu(self):
        while True:
            extra_str = '2: Show User Options'
            print(f"\n\nMenu:\n{'1: Sign in' if self.current_user == None else '1: Sign out'}\n{'2: Sign up' if self.current_user == None else extra_str}\n3: Display Main Page\n4: Quit")
            user_input = input("\nSelect Menu Option: ")

            if user_input == "1":
                if self.current_user == None:
                    username = input("Username = ")
                    password = input("Password = ")

                    signin_data = self.signin(username, password)
                    if signin_data[0] == True:
                        print(signin_data[2])
                        self.set_current_user(signin_data[2])
                        print(signin_data[1])
                    elif signin_data[0] == False:
                        print(signin_data[1])
                else:
                    self.set_current_user(None)
                    print("Signed Out")
            elif user_input == "2":
                if self.current_user == None:
                    username = input("Username = ")
                    password = input("Password = ")
                    name = input("Name = ")
                    age = int(input("Age = "))

                    user = self.signup(name, age, username, password)
                    if user[0] == True:
                        print("User created")
                        print("Signing In...")
                        print("Welcome")
                        self.set_current_user(user[2])
                    else:
                        print(user[1])
                else:
                    self.current_user.display_menu()
            elif user_input == "3":
                self.display_all_posts()
            elif user_input == "4":
                return False
            else:
                print("Invalid Input")

social_media = SocialManager()
social_media.display_menu()
# mike = User("Mike",28)
# social_media.add_user(mike)
# mike.create_user_post("My First Post", datetime.date.today(), "My name is Mike and I just joined this platform today. This is so cooooool!")

# bob = User("Bob",28)
# social_media.add_user(bob)
# bob.create_user_post("My First Post", datetime.date.today(), "My name is Bob, and I do not like mike")

# mike.create_user_post("My Second Post", datetime.date.today(), "This is the second post because im bored")
# mike.delete_user_post(1)

# bob.create_user_post("My Second Post", datetime.date.today(), "Bob. enough said")

# social_media.display_all_posts("DSC")


