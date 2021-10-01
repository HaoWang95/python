"""
Python provides a built-in function called enumerate to address the situation of iterating over length.
enumerate wraps the iterator with a 'lazy-generator' -> Don't worry if u don't understand this, this will covered later.

# game_iterator = enumerate(game_list) -> produces an enumerate object
# when we iterate this enumerate object, we get tuple objects
# then we can unpack a tuple object

- enumerate provides a concise syntax for looping over an iterator and getting the index of each item from the iterator
as we go.
- The first element is index(start from 0 by default), while the second element is the object
"""


def test_loop():
    game_list: list[str] = ['lol', 'dark souls', 'dota', 'overwatch', 'hearthstone']
    # this is how we iterate over a list
    for game in game_list:
        print(f'{game} is very fun')
    # now we need the index of the item to print the ranking of the game
    for i in range(len(game_list)):
        print(f'{i + 1} -> {game_list[i]}')
    # what the above example demonstrates is quite clumsy(but please note the approach above is common in other lang)
    # for(int i = 0; i < game_list.length; i++){
    #     System.out.println(i+1 + " -> " + game_list[i]);
    # }
    # for item in enumerate(game_list):
    #     index, game = item
    #     print(index, game)

    for index, game in enumerate(game_list):
        print(index, game)

    flower_list: list[str] = ['rose', 'lily', 'vanilla']
    for i, flower in enumerate(flower_list):
        print(f'{i+1} - {flower}')


if __name__ == '__main__':
    test_loop()
