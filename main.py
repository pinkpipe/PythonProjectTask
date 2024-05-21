
class User:
    LIST_USERS = []

    def __init__(self, nickname, password, age):
        global LIST_USERS
        self.nickname = nickname
        self.password = password
        self.age = age
        User.LIST_USERS.append(self)


class Video:
    LIST_VIDEOS = []

    def __init__(self, title, duration, time_now, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = adult_mode
        Video.LIST_VIDEOS.append(self)

class UrTube:
    def __init__(self, currant_user):
        self.users = User.LIST_USERS
        self.videos = Video.LIST_VIDEOS
        self.currant_user = currant_user



user1 = User('pink', '12345', 23)

print(user1.nickname, user1.password, user1.age)