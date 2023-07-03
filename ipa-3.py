'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''
social_graph = {
    "@teabetita":{"first_name":"Tea",
                  "last_name":"Betita",
                  "following":[
                  ]
    },
    "@alvarotuason":  {"first_name":"Alvaro",
                  "last_name":"Tuason",
                  "following":[
                      "@teabetita","@werpao"
                  ]
    },
    "@poopie" : {"first_name":"Monica",
                "last_name":"Leonor",
                "following":[
                    "@alexherrera","@alvarotuason","@teabetita","@rosbert"
                ]
    },
    "@werpao":{"first_name":"Paolo",
                   "last_name":"Santos",
                   "following":[
                    "@rosbert","@alvarotuason","@teabetita","@poopie"
                   ]
    },
    "@alexherrera":{"first_name":"Alex",
                  "last_name":"Herrera",
                  "following":[
                    "@teabetita","@poopie","@rosbert"
                  ]
    },
    "@rosbert":  {"first_name":"Reuben",
                  "last_name":"Inumerable",
                  "following":[
                    "@alvarotuason","@werpao"
                  ]
    },
}
def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-3-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph and from_member in social_graph[to_member].get("following"):
        if from_member in social_graph and to_member in social_graph[from_member].get("following"):
            return "friends"
        return "followed by"
    elif from_member in social_graph and to_member in social_graph[from_member].get("following"):
        return "follower"
    else:
        return "no relationship"

print(relationship_status("@alvarotuason", "@teabetita", social_graph))

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        if row[0] != ' ':
            if row.count(row[0]) == len(row):
                return row[0]

    size = len(board)  # Size of the board
    for i in range(size):
        if all(board[j][i] == board[0][i] for j in range(size)):
            return board[0][i]

    diagonal1 = [board[x][x] for x in range(size)]
    diagonal2 = [board[x][size - 1 - x] for x in range(size)]
    if diagonal1.count(diagonal1[0]) == len(diagonal1) and diagonal1[0] != ' ':
        return diagonal1[0]
    if diagonal2.count(diagonal2[0]) == len(diagonal2) and diagonal2[0] != ' ':
        return diagonal2[0]

    return "NO WINNER"

print(tic_tac_toe([
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]))

route_map = {
     ("upd","admu"):{
         "travel_time_mins":15
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","boston"):{
         "travel_time_mins":55
     },
     ("boston","spain"):{
         "travel_time_mins":25
     }
}
def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if (first_stop, second_stop) in route_map:
        travel_time = route_map[(first_stop, second_stop)]["travel_time_mins"]
        return travel_time
    else:
        for x in route_map:
            if x[0] == first_stop:
                first_to_next = route_map[x]["travel_time_mins"]
                if x[1] == second_stop:
                    return first_to_next
                else:
                    next_to_end = eta(x[1], second_stop, route_map)
                    if next_to_end is not None:
                        return first_to_next + next_to_end
    return "nyek invalid route"

print(eta("admu","boston",route_map))