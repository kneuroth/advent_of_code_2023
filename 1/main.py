import re

digit_map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

digit_map_backwards = {
    "orez": 0,
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9
}

NUMBER_REGEX = '(\d)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)'
NUMBER_REGEX_BACKWARDS = '(\d)|(eno)|(owt)|(eerht)|(ruof)|(evif)|(xis)|(neves)|(thgie)|(enin)'

with open('input.txt') as in_file:
    sum = 0
    for line in in_file:
        line = line.rstrip('\n')
        print(line)
        dig1 = re.search(NUMBER_REGEX, line).group()
        dig2 = re.search(NUMBER_REGEX_BACKWARDS, line[::-1]).group()

        if dig1 in digit_map.keys():
            dig1 = digit_map[dig1]
        if dig2 in digit_map_backwards.keys():
            dig2 = digit_map_backwards[dig2]

        #print(line)
        number = int(f"{dig1}{dig2}")
        print(number)
        sum += number
    print(sum)