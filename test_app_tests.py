import datetime 
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from Post import Post
from User import User
from SocialManager import SocialManager

manager = SocialManager()
def test_create_user():
    user1 = FreeUser("Tim", 15)
    assert user1.get_name == "Tim"
    assert user1.get_age == 15

def test_create_post():
    user1 = PremiumUser("Jerome", 900)
    user1.create_user_post("One post", datetime.date.today(), "Stuff")
    user1.create_user_post("Second post", datetime.date.today(), "Nother stuff")

def test_free_user_post_limit():
    user2 = FreeUser("Jim", 18)
    assert  isinstance(user2.create_user_post("My first Post", datetime.date.today(), "I'm the store"), Post) == True
    assert  isinstance(user2.create_user_post("My third Post", datetime.date.today(), "I'm the store"), Post) == True
    assert  isinstance(user2.create_user_post("My third Post", datetime.date.today(), "I'm the store"), Post) == True
    assert  isinstance(user2.create_user_post("This post should equal false", datetime.date.today(), "I'm store"), Post) == False
                       
    
