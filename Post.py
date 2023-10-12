class Post:
    def __init__ (self, title, date_posted, content, id, user):
        self._user = user
        self._id = id
        self._title = title
        self._date_posted = date_posted
        self._content = content

    def __str__ (self):
        return f"{self.get_id} : {self.get_user.get_name} : {self.get_title} : {self.get_date_posted}\n{self.get_content}"
    @property
    def get_user(self):
        return self._user
    
    @property
    def get_id(self):
        return self._id
    @property
    def get_title(self):
        return self._title

    @get_title.setter
    def set_title(self, title):
        if type(title) == str and len(title) > 10:
            self._title = title

    @property
    def get_date_posted(self):
        return self._date_posted

    @get_date_posted.setter
    def set_date_posted(self, date_posted):
        if type(date_posted) == str:
            self._date_posted = date_posted

    @property
    def get_content(self):
        return self._content

    @get_content.setter
    def set_content(self, content):
        if type(content) == str:
            self._content = content