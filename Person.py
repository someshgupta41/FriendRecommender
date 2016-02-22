
class Person:

    def __init__(self, ob):
        self.name = ob['name']
        self.gender = ob["gender"]
        self.location = ob["location"]
        self.age = ob["age"]
        self.school = ob["school"]
        self.prev = ob["previous_location"]
        self.friends = ob["friends"]
        self.friendcount = len(self.friends)
        self.pid = ob["pid"]

    # getters and setter for all individual attributes
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location


    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.name = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_school(self):
        return self.school

    def set_school(self,school):
        self.school = school

    def get_prev(self):
        return self.prev

    def set_prev(self,prev):
        self.prev = prev


    def get_friends(self):
        return self.friends

    def set_friends(self,friends):
        self.friends = friends

    def get_friendcount(self):
        return self.friends

    def set_friendcount(self,friendcount):
        self.friends = friendcount


    def get_pid(self):
        return self.pid

    def set_pid(self,pid):
        self.pid = pid
