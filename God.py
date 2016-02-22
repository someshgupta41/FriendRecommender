from geopy.distance import great_circle
from geopy.geocoders import Nominatim

import Relationship
import Person
import Queue as Q
import time

class God:

    def __init__(self, data_obj):
        self.person_count = 0
        self.list_of_pids = [0]
        self.person_list = [None]
        self.create_world(data_obj)
        self.relationship_book = Relationship.Relationship(data_obj)
        print "God RAM have created relationship book as well! :) \n"

    def create_world(self, data_obj):
        """
        This Function will create world fr GOD
        :param data_obj:
        :return:
        """

        print "God RAM have started creating the world!\n"
        if data_obj == None:
            return
        else:
            for data_instance in data_obj['persons']:
                self.person_list.append(Person.Person(data_instance))
                self.person_count += 1
                self.list_of_pids.append(self.person_list[-1].get_pid())
        print "God RAM have finished creating the world!\n"

    def update_person_details(self, pid, new_details):
        """
        This is Person update utility function
        :param pid: pid of the person who's details are to be updated
        :param new_details:  This is list of dict obj which are to be updated
        :return: 1 if success else failure
        """

        if pid in self.person_list:
            for pid in self.person_list:
                self.person_list[pid].name = new_details["name"]
                self.person_list[pid].gender = new_details["gender"]
                self.person_list[pid].location = new_details["location"]
                self.person_list[pid].age = new_details["age"]
                self.person_list[pid].school = new_details["school"]
                self.person_list[pid].prev = new_details["prev"]
                self.person_list[pid].friends = new_details["friends"]
                self.person_list[pid].friendcount = len(new_details["friends"])
                return 1
        else:
            return -1

    def find_recommendations(self, pid):
        """
        Returns 6 Recommended pid's:
            3 Mututal friend's based recommendations
            3 recommendations based on school, age and proximity
        :param pid: Pid of the person for which recommendations are required
        :return: list of pid's
        """

        all_friends = set()
        p_friends = self.relationship_book.get_all_friends(pid)
        for p_friend in p_friends :
            for p_f_friend in self.relationship_book.get_all_friends(p_friend):
                if (p_f_friend not in p_friends) and p_f_friend != pid: # Excluding current friends and himself/herself
                    all_friends.add(p_f_friend)

        prio_q = Q.PriorityQueue()
        for p_f_friend in all_friends:
            p_f_f_friend = self.relationship_book.get_all_friends(p_f_friend)

            # intersection of y and p_friends
            no_of_mutual_friends  = len(list(set(p_f_f_friend) & set(p_friends)))
            prio_q.put((-no_of_mutual_friends, p_f_friend))
                # priority_queue, with (-ve score, id), negative score to build a min-heap

            if prio_q.qsize() > 3: # 3 recommendations of such kind
                prio_q.get()

        recommended_pids = set()
        for itr in range(prio_q.qsize()):
            recommended_pids.add(prio_q.get()[1])

        # @todo: check and clear prio_q explicitely here
        start_time = time.time()
        print "\n\nIt takes time to give you good suggestions. Well, We know distance matters!\nBe patient :) "
        for p_f_friend in all_friends:
            school_score = self.do_they_have_same_school(pid, p_f_friend)
            age_score = self.do_they_have_same_age_group(pid, p_f_friend)

            proximity_score = self.do_they_live_closeby(pid, p_f_friend)

            score = school_score + age_score + proximity_score
            prio_q.put((-score, p_f_friend))
                # priority_queue, with (-ve score, id), negative score to build a min-heap

            if prio_q.qsize() > 3: # 3 recommendations of such kind
                prio_q.get()

        print("It took us %s seconds to find you, your new friends... But here is the fruit of patience!" % (time.time() - start_time))
        for itr in range(prio_q.qsize()):
            recommended_pids.add(prio_q.get()[1])

        return list(recommended_pids)


    def do_they_have_same_school(self, pid1, pid2):
        return self.person_list[pid1].school == self.person_list[pid2].school

    def do_they_have_same_age_group(self, pid1, pid2):
        return abs(self.person_list[pid1].age-self.person_list[pid2].age) < 5

    def do_they_live_closeby(self, pid1, pid2):
        return self.get_dist(pid1, pid2) < 25 # 25 miles

    def get_person(self, pid):
        """
        :param pid: pid of person who's details are required
        :return: Person Object
        """
        return self.person_list[pid]

    def get_person_list(self, list_of_pids):
        """
        :param list_of_pids: list of pid's whose details are required
        :return: list of Person objects
        """
        return [self.person_list[i] for i in list_of_pids]



    def get_dist(self, pid1, pid2):

        geolocator = Nominatim()
        location1 = geolocator.geocode(self.get_person(pid1).get_location())
        location2 = geolocator.geocode(self.get_person(pid2).get_location())

        first_place = (location1.latitude,location1.longitude)
        second_place = (location2.latitude,location2.longitude)

        # get distance of location 1&2 in miles
        return (great_circle(first_place,second_place).miles)
