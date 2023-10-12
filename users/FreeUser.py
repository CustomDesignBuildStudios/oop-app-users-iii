from User import User
from Post import Post
class FreeUser(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def create_user_post(self, title, date, content):
        
        if len(self._posts) < 3:
            return super().create_user_post(title, date, content, self)
            # post = Post(title, date, content, User.add_post())
            # self._posts.append(post)
            # return post
        return None
    
