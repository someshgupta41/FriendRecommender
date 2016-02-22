import God
import json


class Messenger:

    def __init__(self, big_bang_file):
        print "Messenger HANUMAN is here! :)\n"
        self.ram = self.wake_up_god(big_bang_file)

    # Wakes up God, and he creates world and relationship_book
    def wake_up_god(self, big_bang_file):

        print "God RAM was called! He woke up!\n"

        data = None
        with open(big_bang_file, 'r') as file:
            data = json.load(file)
        return God.God(data)

    # All helper functions, sending messages to GOD (For all supported query types)
    def provide_recommendations(self, pid):
        return self.ram.find_recommendations(pid)

    def update_relationship(self, pid1, pid2):
        pass

    def add_person(self, person_detail_object):
        pass



