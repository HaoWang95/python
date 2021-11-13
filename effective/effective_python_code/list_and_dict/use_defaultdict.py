from typing import Dict, Set
from collections import defaultdict

"""
In this file, we compare the differences of setdefault and defaultdict. And let's get started with a simple senario.
We would like to keep track of cities that we've visited around the world using a dictionary that maps country name to
a set instance containing the corresponding city names.
1. When the country name needs to map to a **set** of city names? -> Because data in set is not repeatable
"""


def use_setdefault() -> None:
    visited_country: Dict[str, Set[str]] = {
        "Australia": {"Melbourne"},
    }
    # If we want to know whether we've been to France before, and this is my first time to be in France, the city is
    # Paris
    visited_country.setdefault("France", set()).add("Paris")
    # If we want to know whether we've been to Australia before, and the city I've visited is Sydney
    visited_country.setdefault("Australia", set()).add("Sydney")
    # How to achieve this using get? Say I would like to know whether I've visited Japan before, and now I'm visiting
    # Kyoto
    visited_country.setdefault("Japan", set()).add("Kyoto")
    # I would like to know whether I have visited Germany, if so, this time I'm visiting Munich
    visited_country.setdefault("Germany", set()).add("Munich")
    print(visited_country)


def use_defaultdict():
    """
    The defaultdict class from collections built-in module simplifies the common use case by automatically storing a
    default value when the key does not exist.
    :return: None
    """
    my_visited_countries: Dict[str, Set[str]] = defaultdict(set)
    my_visited_countries["Australia"].add("Melbourne")
    my_visited_countries["Australia"].add("Sydney")
    print(my_visited_countries)


# Now we use setdefault to construct our own data structure called visits
class VisitedCountry:
    def __init__(self):
        self.__visited: Dict[str, Set[str]] = {}

    def add(self, country, city):
        if country is not None and city is not None:
            self.__visited.setdefault(country, set()).add(city)
        else:
            raise Exception()

    def __repr__(self):
        return repr(self.__visited)


# How to convert the example above, to use defaultdict instead of setdefault ?
class DefaultVisitedCountry:
    def __init__(self):
        self.__visited = defaultdict(set)

    def add(self, country: str, city: str) -> None:
        if country is None or city is None:
            raise Exception()
        self.__visited[country].add(city)

    def __repr__(self):
        return repr(self.__visited)


if __name__ == '__main__':
    # use_setdefault()
    use_defaultdict()
    my_visited_list = VisitedCountry()
    my_visited_list.add("Australia", "Melbourne")
    print(my_visited_list)
