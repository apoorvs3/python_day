class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0  # we can have a default value as well
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(2, 'angela')
user2 = User(3, 'vohoo')
print(user1.name)

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
