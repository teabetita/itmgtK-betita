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

print(eta("admu","spain",route_map))