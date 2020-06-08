#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create dict of sources and destinations
    tickets_dict = {ticket.source: ticket.destination for ticket in tickets}
    # create route list with initial destination
    route = [tickets_dict['NONE']]
    # loop through number of tickets exempting the first one
    for i in range(1, length):
        # using the initial destination in routes list as a source append each destination
        route.append(tickets_dict[route[i-1]])
    # return routes list
    return route
