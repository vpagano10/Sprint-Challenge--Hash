#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        # source = start airport
        self.destination = destination
        # destination = next airport


def reconstruct_trip(tickets, length):
    routes = dict()
    routes_tracker = []

    for i in tickets:
        routes[i.source] = i.destination

    for key in routes.keys():
        print(key)
    routes_tracker.append(routes["NONE"])
    for i in routes_tracker:
        if routes[i] == "NONE":
            routes_tracker.append("NONE")
            break
        else:
            routes_tracker.extend([routes[i]])

    return routes_tracker


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)
