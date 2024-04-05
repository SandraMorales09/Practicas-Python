from enum import Enum

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4
def tetris():

    screen = [["🔳", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["🔳", "🔳", "🔳", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"], 
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"], 
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"],
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"], 
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"], 
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"], 
              ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]] 

    print_screen(screen)


def move__piece(movement: Movement): 
    new_row_index = 0
    new_column_index = 0

    for row_index, in enumerate(screen):
        for column_index, column in enumerate(row):

            match movement:
                case Movement.DOWN:
                    new_row_index = row_index + 1
                    new_column_index = column_index        
                case Movement.RIGHT:

                case Movement.LEFT:

                case Movement.ROTATE: 
    
def print_screen(screen: List):
    for row in screen:
    print(".join"(map(str, row)))              

tetris()             