import re
colors = ['red', 'green', 'blue']

COLOR_REGEX = '(red)|(green)|(blue)'

def check_reveal_valid(cube_map):
    good_cube_map = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for key in good_cube_map.keys():
        sum = 0
        if key in cube_map:
            sum += cube_map[key]
            if cube_map[key] > good_cube_map[key]:
                return False
            if sum > 12 + 13 + 14:
                return False
    return True


valid_games = {}
sum = 0
power_sum = 0
with open('input.txt') as in_file:
  
    for game in in_file:
        game = game.rstrip('\n')
        
        game_num = int(game.split(':')[0].split(' ')[1])
        game_is_valid = True

        max_cube_map = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        print(game)
        
        for reveal in game.split(';',):
            reveal = reveal.split(',')
            cube_map = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for cubes in reveal:
                # Cube loop
                match = re.search(COLOR_REGEX, cubes)
                span = match.span()
                color = cubes[match.span()[0]:match.span()[1]]
                quantity = int(cubes[match.span()[0]-3:match.span()[0]])

                # Set new maximum
                if quantity > max_cube_map[color]:
                    max_cube_map[color] = quantity
                
                cube_map[color] += quantity

            # Reveal loop
            if (not check_reveal_valid(cube_map)):
                game_is_valid = False
        
        
        # Get cube power and add to sum
        product = 1
        for value in max_cube_map.values():
            product = product * value
        power_sum += product

        # Game loop
        if game_is_valid:
            sum += game_num
        
print("Valid game sum:", sum)
print("Power sum:", power_sum)

# goods = [{
#     "red": 1,
#     "green": 5,
#     "blue": 2
# },
# {
#     "red": 3,
#     "blue": 2
# },{
#     "red": 12,
#     "green": 13,
#     "blue": 14
# }]

# bads = [{
#     "red": 150,
#     "green": 5,
#     "blue": 2
# },
# {
#     "red": 13,
#     "blue": 12,
#     "green": 12
# }]

# for item in goods:
#     print(check_reveal_valid(item))