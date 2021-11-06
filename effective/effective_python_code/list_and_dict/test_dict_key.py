from typing import Dict

"""
In this file, we will investigate deeply at how many approaches we can use to check if a key exists in a dict.
1. In method test_key_in_dict(key), given the parameter key, try if you can see if this key exists in the default dict.
"""


def test_key_in_dict(key: str) -> bool:
    """
    In this method, we will initialise a dict called players, that contains player name as keys, and the corresponding
    player score as values.
    player: dict(str, int) = {}
    :return: bool -> true, exists; false, non-exists
    """
    players: Dict[str, int] = {
        "Albert": 0,
    }
    try:
        if players[key] is not None:
            return True
    except KeyError:
        return False


def test_key_in_dict2(key: str = None) -> bool:
    """
    :param key:
    :return: bool, True exists, False not exists
    """
    players: Dict[str, int] = {
        'Peter': 0,
        'Albert': 1,
    }
    # based on our testing, players.keys() returns a dict_keys object, which is an Iterable
    if key is not None:
        if key in players.keys():
            return True
    return False


def test_key_in_dict3(key) -> bool:
    """
    For a dictionary with simple types, using the get method is the shortest and clearest option
    :param key:
    :return:
    """
    players = {
        'John': 0
    }
    if players.get(key) is not None:
        return True
    return False


def update_score(player: str, dashboard: Dict[str, int]):
    if dashboard.get(player) is not None:
        dashboard[player] += 1
    else:
        dashboard[player] = 0


if __name__ == '__main__':
    player_name: str = 'Albert'
    print(f'{test_key_in_dict.__name__} -> {player_name}: {test_key_in_dict(player_name)}')
    if test_key_in_dict(player_name):
        print(f'{player_name} is in players dict')
    else:
        print(f'{player_name} is not in players dict')
    print(f'{test_key_in_dict2.__name__} -> {player_name}: {test_key_in_dict2(player_name)}')
    print(f'{test_key_in_dict3.__name__} -> {player_name}: {test_key_in_dict3(player_name)}')
    player_dashboard: Dict[str, int] = {
        'Albert': 0
    }
    update_score(player_name, dashboard=player_dashboard)
    print(player_dashboard)
    update_score('John', player_dashboard)
    print(player_dashboard)
    update_score('Peter', player_dashboard)
    print(player_dashboard)
