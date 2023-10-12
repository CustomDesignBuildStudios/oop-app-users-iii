# your User class goes here
import datetime 
from Post import Post

class User:
    posts_created = 0

    @classmethod
    def add_post(cls):
        cls.posts_created += 1
        return cls.posts_created

    @classmethod
    def get_total_created_posts(cls):
        return cls.posts_created

    # @classmethod
    # def display_main_page(cls):
    #     posts_string = ""
    #     for item in cls.posts:
    #         posts_string += str(item) + " \n"
    #     return f"All Posts:\n{posts_string}"
 

    # @classmethod
    # def create_new_post(cls, user, title, date_posted, content):
    #     new_post = Post(user,title, date_posted, content, cls.posts_created)
    #     cls.posts.append(new_post)
    #     cls.posts_created += 1
    #     user.create_user_post(new_post)
    #     return new_post
    
    # @classmethod
    # def delete_post(cls, id):
    #     for index in range(len(cls.posts)):
    #         if cls.posts[index].get_id == id:
    #             cls.posts[index].get_user.delete_user_post(index)
    #             del cls.posts[index]


    def __init__ (self, name, age, username, password):
        self.set_name = name
        self.set_username = username
        self.set_password = password
        self.set_age = age
        self._posts = []
        self.set_type = "Free"
    def __str__ (self):
        posts_string = ""
        for item in self.get_posts:
            posts_string += str(item) + " \n"
        return f"Hello I'm {self._name} and I am {self._age} years old. Welcome to my page:\nPosts:\n{posts_string}"

    @property
    def get_username(self):
        return self._username

    @get_username.setter
    def set_username(self, value):
        self._username = value

    @property
    def get_password(self):
        return self._password

    @get_password.setter
    def set_password(self, value):
        self._password = value

    @property
    def get_type(self):
        return self._type

    @get_type.setter
    def set_type(self, value):
        self._type = value

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, value):
        self._name = value

    @property
    def get_posts(self):
        return self._posts

    @get_posts.setter
    def set_posts(self, posts):
        if type(posts) == dict:
            self._posts = posts


   
    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, age):
        if age > 13:
            self._age = age 


    def create_user_post(self, title, date_posted, content):
        post = Post(title, date_posted, content, User.add_post(), self)
        self._posts.append(post)
        return post

    def delete_user_post(self, post_id):
        for index in range(len(self._posts)):
            if post_id == self._posts[index]._id:
                del self._posts[index]
                return
    
    def display_posts(self, order = "ASC"):
        all_posts = sorted(self.get_posts, key=lambda obj: obj._id)

        print(f"Posts:")
        if order == "DSC":
            all_posts = reversed(all_posts)

        for post in all_posts:
            print(post)    


    def display_menu(self):
        while True:
            print("\n\nUser Menu:\n1: Add post\n2: Delete Post\n3: Display Posts\n4: Go Back to Main Menu")
            user_input = input("\nSelect Menu Option: ")

            if user_input == "1":
                post_title = input("Post Title = ")
                post_body = input("Post Body = ")

                self.create_user_post(post_title, datetime.date.today(),  post_body)
                print("Post Added")
            elif user_input == "2":
                self.display_posts()
                delete_id = int(input("Which post would you like to delete? "))
                self.delete_user_post(delete_id)
            elif user_input == "3":
                self.display_posts()
            elif user_input == "4":
                return False
            else:
                print("Invalid Input")

    

