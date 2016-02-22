import json

from geopy.distance import great_circle
from geopy.geocoders import Nominatim

import Messenger


# creating messenger
print "Messenger HANUMAN was called!\n"
hanuman = Messenger.Messenger('input.json')

query_code = 0

# @todo: define all query codes here & describe

while query_code != -1: # query_code = -1, defines terminating condition

    query_code = int(raw_input("\nEnter the query code which you want to perform: "))

    if query_code == 1: # for recommendations
        pid = int(raw_input("Enter the pid of person for whome you want recommendations!"))

        print hanuman.provide_recommendations(pid)

    elif query_code == 2:   # Update Person Details
        pass

    elif query_code == 3:   # Add person
        pass

    elif query_code == 4:   # add a relationship
        pass

    elif query_code == -1:
        print "This is end of the world!!!"
        break



