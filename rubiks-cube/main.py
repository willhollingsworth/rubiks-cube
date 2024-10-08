
class Cube():
    ''' A class to represent a Rubik's Cube '''
   
    colours = 'OBWRYG'
    width = 3
    height = width * 4

    def __init__(self, initial_state: str = ''):
        self.horizontal_rows = self.determine_horizontal_rows()
        if len(initial_state) < 1:
            initial_state = self.build_default_string()
        self.state : list[list] = self.build_state(initial_state)

    def __repr__(self)  -> str:
        ''' output a string of the current state of the cube '''
        separator = ' '
        string = ''
        for i, line in enumerate(self.state):
            line_string = separator.join([item for item in line]) + '\n'
            if i not in self.horizontal_rows:
                # if not a horizontal row, add space offsets to help allign the string output
                line_string = separator * 6 + line_string
            string += line_string
        return string

    def determine_horizontal_rows(self) -> list[int]:
        ''' determine which rows of the cube are the longer horizontal rows'''
        horizontal_rows: list = list(range(self.width * 4))
        start_slice: int = self.width * 2        
        end_slice: int = self.width * 3
        return horizontal_rows[start_slice : end_slice]

    def build_state(self, cube_string: str) -> list[list[str]]:
        '''
        Build a cube from a string
        the format is a long string of colours going left to right, top to bottom
        the unwrapped cube is a reversed cross shape
        an example below with each character representing it's 3x3 grid
            r
            g
          w b y
            o
        '''
        cube: list[list] = []
        start: int = 0
        end: int = 0
        for row in range(self.height):
            if row in self.horizontal_rows:
                end += self.width * 3
            else:
                end += self.width
            sliced_string: str = cube_string[start : end]
            row_list: list = [c for c in sliced_string]
            cube.append(row_list)
            if row in self.horizontal_rows:
                start += self.width * 3
            else:
                start += self.width
        return cube
        
    def build_default_string(self) -> str: 
        ''' 
        build a default string using the objects colours
        ended up being more complicated and hacky than I wanted due to the wide horizontal rows
        '''
        cube_string: str = ''
        for row in range(self.height):
            colour_index:int = int(row / self.width)
            if row < self.horizontal_rows[0]:
              cube_string += self.colours[colour_index] * 3
            elif row in self.horizontal_rows:
                for h_row in self.horizontal_rows:
                    colour_index: int = int(h_row - self.width - 1)
                    cube_string += self.colours[colour_index] * 3
            elif row > self.horizontal_rows[-1]:
                cube_string += self.colours[-1] * 3
        return cube_string
    
    def rotate(self, direction: bool = True, layer: int = 0) -> None:
        ''' 
        Rotate a layer of the cube in a given direction 
        Direction: true for right or up
        Layer: start counting from the top left along to the top right, then down to the bottom right
        Example:
        0 1 2
        X X X 3
        X X X 4
        X X X 5
        '''
        is_horizontal_rotate: bool = layer >= self.width
        
        if is_horizontal_rotate:
            row = layer + self.width
            if direction:
                # shift row to the right
                self.state[row] = self.state[row][-self.width:] + self.state[row][:-self.width]
            else:    
                # shift row to the left
                self.state[row] = self.state[row][self.width:] + self.state[row][:self.width]
            

if __name__ == '__main__':
    cube = Cube()
    print(cube)
    cube.rotate(layer=4, direction=False)
    print(cube)
    cube.rotate(layer=4, direction=False)

