1
class Relationship:

    def __init__(self, data_obj):

        self.relationships = self.get_relationships(data_obj)
            # This is a list of list; relationships[i] would give a list of friends of person with pid 'i'


    def get_relationships(self,data_obj):
        if data_obj == None:
            return

        temp = [[] for i in range(len(data_obj['persons'])+1)]
        for data_instance in data_obj['persons']:
            friends = map(int, data_instance['friends'].split(","))
            temp[data_instance['pid']].extend(friends)
            for friend in friends:
                temp[friend].append(data_instance['pid'])
        return temp

    def get_all_friends(self, pid):
        """
        :param pid: pid of person whose friend's pids are required
        :return: return a list of pid's
        """
        return self.relationships[pid]

    def are_they_friends(self, pid1, pid2):
        j = 1
        for p in self.get_all_friends(pid1):
            if p == pid2:
                j = 0
                return True
            else:
                continue
        if j == 1:
            return False

    # @todo: Add  and remove relationship
    def add_relationship(self, pid1, pid2):
        pass

    def remove_relationship(self, pid1, pid2):
        pass


