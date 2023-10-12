from User import User
class PremiumUser(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.set_type = "premium"

