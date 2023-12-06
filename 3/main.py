

def get_left_coords(row, col):
    # Cn = Element coordinates returned by this function
    # 5 = Number corresponding to row and col parameters
    # . . C1
    # . . C2 5
    # . . C3
    C1 = [row - 1, col - 1]
    C2 = [row, col - 1]
    C3 = [row + 1, col - 1] 
    return (C1, C2, C3)

def get_right_coords(row, col):
    # Cn = Element coordinates returned by this function
    # 5 = Number corresponding to row and col parameters
    # . . . . C1
    # . . . 5 C2
    # . . . . C3
    C1 = [row - 1, col + 1]
    C2 = [row, col + 1]
    C3 = [row + 1, col + 1]
    return (C1, C2, C3)

def get_vertical_coords(row, col):
    # Cn = Element coordinates returned by this function
    # 5 = Number corresponding to row and col parameters
    # . . . C1 .
    # . . .  5 .
    # . . . C2 .
    C1 = [row - 1, col]
    C2 = [row + 1, col]
    return (C1, C2)

def determine_character(coord, grid):
    x, y = coord
    if x < 0 or y < 0:
        return '-1'
    try:
        return grid[coord[0]][coord[1]]
    except IndexError:
        return '-1'

def is_part_number(coords, grid):
    x = coords[0]
    y = coords[1]
    coord_value: str = grid[x][y]
    if coord_value.isnumeric() and coord_value != '-1':
        left_coords = get_left_coords(x, y)
        right_coords = get_right_coords(x, y)
        vertical_coords = get_vertical_coords(x, y)
        coords = (*left_coords, *right_coords, *vertical_coords)
        for coord in coords:
            char: str = determine_character(coord, grid)
            if char not in ['.', '-1'] and not char.isnumeric():
                # character should be a symbol
                return True
    return False

def is_gear_number(coords, grid):
    x = coords[0]
    y = coords[1]
    coord_value: str = grid[x][y]
    if coord_value.isnumeric() and coord_value != '-1':
        left_coords = get_left_coords(x, y)
        right_coords = get_right_coords(x, y)
        vertical_coords = get_vertical_coords(x, y)
        coords = (*left_coords, *right_coords, *vertical_coords)
        for coord in coords:
            char: str = determine_character(coord, grid)
            if char == '*':
                # character should be a symbol
                return coord
    return False

def add_to_gear_map(key, value, gear_map):
    try:
        if gear_map[key]:
            gear_map[key].append(value)
    except KeyError:
        gear_map[key] = [value]


grid = []
sum = 0
gear_map = {}

with open('input.txt') as in_file:
    for line in in_file:
        # Split string into list
        grid.append([*line.split('\n')[0]])
        print(line)

# Part 2 loop
for row_num, row in enumerate(grid):
    print(row)
    in_number = False
    in_gear_number = False
    number_concat = ""
    gear_coord = []
    for col_num, value in enumerate(row):
        # Iterate over each value
        # If we see a number, stop, set is_number = true
        # Then check left, right and vertical
        # If a * is found, set is_gear_number = true
        # iterate and append numbers until non-number is found
        # Set is_number = false
        # Set is_gear_number = false
        gear = is_gear_number([row_num, col_num], grid)
        if gear:
            # We have found a gear number
            in_gear_number = True
            number_concat += value
            gear_coord = gear

            # Edge case for literal edge of grid
            if col_num == len(row) - 1:
                # convert number_concat to int and add it to gear_map
                print(number_concat, " is a gear number touching", gear_coord)
                key = f'{str(gear_coord[0])},{str(gear_coord[1])}'
                add_to_gear_map(key, int(number_concat), gear_map)

        elif value.isnumeric():
                # We have a number, but not neccesarily a gear number
                in_number = True
                number_concat += value

                # Edge case for literal edge of grid
                if col_num == len(row) - 1 and in_gear_number:
                    # convert number_concat to int and add it to gear_map
                    print(number_concat, " is a gear number touching", gear_coord)
                    key = f'{str(gear_coord[0])},{str(gear_coord[1])}'
                    add_to_gear_map(key, int(number_concat), gear_map)

        else:
            # We found a symbol or .
            if in_gear_number:
                # convert number_concat to int and add it to gear_map
                print(number_concat, " is a gear number touching", gear_coord)
                key = f'{str(gear_coord[0])},{str(gear_coord[1])}'
                add_to_gear_map(key, int(number_concat), gear_map)

            # Reset running variables
            in_gear_number = False
            in_number = False
            number_concat = ""

# Part 2 loop 2
for gear in gear_map.values():
    if len(gear) == 2:
        sum += gear[0] * gear[1]

# Part 1 loop
# for row_num, row in enumerate(grid):
#     print(row)
#     in_number = False
#     in_part_number = False
#     number_concat = ""
#     for col_num, value in enumerate(row):
#         #print(value)
#         # Iterate over each value
#         # If we see a number, stop, set is_number = true
#         # Then check left, right and vertical
#         # If a symbol is found, set is_part_number = true
#         # iterate and append numbers until non-number is found
#         # Set is_number = false
#         # Set is_part_number = false
#         if is_part_number([row_num, col_num], grid):
#             # We have found a part number
#             in_part_number = True
#             number_concat += value

#             # Edge case for literal edge of grid
#             if col_num == len(row) - 1:
#                 # convert number_concat to int and add it to sum
#                 sum += int(number_concat)
#                 print(number_concat, " is a part number")

#         elif value.isnumeric():
#                 # We have a number, but not neccesarily a part number
#                 in_number = True
#                 number_concat += value

#                 # Edge case for literal edge of grid
#                 if col_num == len(row) - 1 and in_part_number:
#                     # convert number_concat to int and add it to sum
#                     sum += int(number_concat)
#                     print(number_concat, " is a part number")
#         else:
#             # We found a symbol or .
#             if in_part_number:
#                 # convert number_concat to int and add it to sum
#                 sum += int(number_concat)
#                 print(number_concat, " is a part number")

#             # Reset running variables
#             in_part_number = False
#             in_number = False
#             number_concat = ""
    
print(sum)
# TESTING
# test_grid = [
#     ['.', '.', '.'],
#     ['.', '5', '.'],
#     ['.', '.', '#'],
#     ['6', '.', '.'],
#     ['.', '&', '.']]

# print(determine_character([1, 1], test_grid)) # 5
# print(determine_character([2, 1], test_grid)) # .
# print(determine_character([2, 2], test_grid)) # #
# print(determine_character([5, 0], test_grid)) # -1
# print(determine_character([-1, 2], test_grid)) # -1
# print(determine_character([3, 4], test_grid)) # -1

# Expect 5, ., #, -1, -1, -1,



#print(is_part_number([3, 0], test_grid))