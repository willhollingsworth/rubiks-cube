
class Cube():
    default_state = [
    ['o', 'o', 'o'],
    ['o', 'o', 'o'],
    ['o', 'o', 'o'],
    ['b', 'b', 'b'],
    ['b', 'b', 'b'],
    ['b', 'b', 'b'],
    ['w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
    ['w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
    ['w', 'w', 'w', 'r', 'r', 'r', 'y', 'y', 'y'],
    ['g', 'g', 'g'],
    ['g', 'g', 'g'],
    ['g', 'g', 'g'],
    ]
    def __init__(self,initial_state = default_state):
        self.state : list[list] = initial_state
        self.horizontal_rows = [i for i, row in enumerate(self.state) if len(row) > 3]

    def print_state(self):
        ''' print the current state of the cube '''
        separator = ' '
        for i, line in enumerate(self.state):
            statement = separator.join([item for item in line])
            if i not in self.horizontal_rows:
                statement = separator * 6 + statement
            print(statement)


if __name__ == '__main__':
    cube = Cube()
    cube.print_state()

