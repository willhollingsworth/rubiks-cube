
class Cube():
    ''' A class to represent a Rubik's Cube '''
   
    colours = 'OBWRYG'
    width = 3
    height = width * 4

    def __init__(self, initial_state: str = ''):
        self.horizontal_rows_index = self.determine_horizontal_rows_index()
        if len(initial_state) < 1:
            initial_state = self.build_default_string()
        self.state : list[list] = self.build_state(initial_state)

    # MARK:Repr
    def __repr__(self)  -> str:
        ''' output a string of the current state of the cube '''
        separator = ' '
        string = ''
        for i, line in enumerate(self.state):
            line_string = separator.join([item for item in line]) + '\n'
            if i not in self.horizontal_rows_index:
                # if not a horizontal row, add space offsets to help align the string output
                line_string = separator * 6 + line_string
            string += line_string
        return string
    
    # MARK:Rows
    @property
    def rows(self) -> list[list[str]]:
        ''' return the horizontal rows of the cube '''
        start = self.horizontal_rows_index[0]
        stop = self.horizontal_rows_index[-1] + 1
        return self.state[start : stop]
    
    @rows.setter
    def rows(self, input: tuple[int, list[str]]) -> None:
        ''' 
        set a horizontal row using a tuple of the index and row values
        '''
        index = input[0]
        value = input[1]
        index += self.width * 2
        self.state[index] = value

    # MARK:Columns
    @property
    def columns(self) -> list[list[str]]:
        ''' return the vertical columns of the cube '''
        columns : list[list[str]] = []
        for column_index in range(self.width):
            columns.append([])
            for row_index in range(self.height):
                is_horizontal_row = row_index in self.horizontal_rows_index
                column_index_shifted = column_index
                if is_horizontal_row:
                    column_index_shifted += self.width
                row = self.state[row_index][column_index_shifted]
                columns[column_index].append(row)
        return columns

    @columns.setter
    def columns(self, input: tuple[int, list[str]]) -> None:
        ''' 
        set a horizontal row using a tuple of the index and row values
        '''
        index = input[0]
        value = input[1]
        for row_index in range(self.height):
            is_horizontal_row = row_index in self.horizontal_rows_index
            column_index_shifted = index
            if is_horizontal_row:
                column_index_shifted += self.width
            self.state[row_index][column_index_shifted] = value[row_index]

    # MARK:H rows index
    def determine_horizontal_rows_index(self) -> list[int]:
        ''' determine which rows of the cube are the longer horizontal rows'''
        horizontal_rows: list = list(range(self.width * 4))
        start_slice: int = self.width * 2        
        end_slice: int = self.width * 3
        return horizontal_rows[start_slice : end_slice]
    
    # MARK: Build State
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
            if row in self.horizontal_rows_index:
                end += self.width * 3
            else:
                end += self.width
            sliced_string: str = cube_string[start : end]
            row_list: list = [c for c in sliced_string]
            cube.append(row_list)
            if row in self.horizontal_rows_index:
                start += self.width * 3
            else:
                start += self.width
        return cube
    
    # MARK: B default string
    def build_default_string(self) -> str: 
        ''' 
        build a default string using the objects colours
        ended up being more complicated and hacky than I wanted due to the wide horizontal rows
        '''
        cube_string: str = ''
        for row in range(self.height):
            colour_index:int = int(row / self.width)
            if row < self.horizontal_rows_index[0]:
              cube_string += self.colours[colour_index] * 3
            elif row in self.horizontal_rows_index:
                for h_row in self.horizontal_rows_index:
                    colour_index: int = int(h_row - self.width - 1)
                    cube_string += self.colours[colour_index] * 3
            elif row > self.horizontal_rows_index[-1]:
                cube_string += self.colours[-1] * 3
        return cube_string
    
     # MARK: Rotate Horizontal
    def rotate_horizontal(self, direction: bool = True, row_index: int = 0) -> None:
        ''' 
        Rotate a horizontal row of the cube, counting from top to bottom
        '''
        row = self.rows[row_index]
        offset = self.width
        if direction:
            # shift row to the right
            row = row[-offset:] + row[:-offset]
        else:    
            row = row[offset:] + row[:offset]
        # shift row to the left
        self.rows = (row_index, row)

     # MARK: Rotate Horizontal
    def rotate_vertical(self, direction: bool = True, column_index: int = 0) -> None:
        ''' 
        Rotate a vertical column of the cube, counting from left to right
        '''
        column = self.columns[column_index]
        offset = self.width
        if direction:
            # shift column up
            column = column[offset:] + column[:offset]
        else:    
            # shift column down
            column = column[-offset:] + column[:-offset]
        self.columns = (column_index, column)

# MARK: Main
if __name__ == '__main__':
    cube = Cube()
    print(cube)
    cube.rotate_horizontal(row_index = 0)
    cube.rotate_horizontal(row_index = 1)
    cube.rotate_horizontal(row_index = 2)
    # cube.rotate_vertical(False, 0)

    # print(cube)
    # cube.columns = (2, [c for c in 'BBBRRRGGGOOO'])
    # for row in cube.columns:
    #     for item in row:
    #         print(item, end=' ')
    #     print()
    # print(cube.columns)
    print(cube)
    # print(cube)
    # for i in "hi 123    carla":
        # print(i)
    # print(cube)



