capitals = {
    'france': 'paris',
    'Germany': 'Berlin'
}
print(capitals['france'])

# Dictionary in a dictionary
travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'Cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits': 34}
}
print(travel_log['Germany'])

# Dictionary in a list

travel_log_1 = {
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        'country': 'Germany',
        'Cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 34
    }
}
