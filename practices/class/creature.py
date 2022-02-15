class Creature:
    def __init__(self, species: str) -> None:
        self.species = species

    @classmethod
    def from_data(cls, species):
        return cls(species=species)

    def __repr__(self):
        return f'{self.species}'


class Human(Creature):
    def __init__(self, species):
        super().__init__(species)


if __name__ == '__main__':
    alan = Human.from_data('people')
    print(alan)
