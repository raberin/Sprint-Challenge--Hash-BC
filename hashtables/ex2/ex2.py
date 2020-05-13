#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    for i in range(len(tickets)):
        # Insert ticket into a hashtable source:destination
        print(tickets[i].source)
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    # Appened first destination of the route
    route[0] = hash_table_retrieve(ht, "NONE")
    # Loop through the rest using the first destination to retrieve key:values
    for i in range(1, len(route)):
        route[i] = hash_table_retrieve(ht, route[i - 1])
    return route


# tickets = [
#     Ticket("PIT",  "ORD"),
#     Ticket("XNA",  "CID"),
#     Ticket("SFO",  "BHM"),
#     Ticket("FLG",  "XNA"),
#     Ticket("NONE",  "LAX"),
#     Ticket("LAX",  "SFO"),
#     Ticket("CID",  "SLC"),
#     Ticket("ORD",  "NONE"),
#     Ticket("SLC",  "PIT"),
#     Ticket("BHM",  "FLG")
# ]

# print(reconstruct_trip(tickets, 9))
