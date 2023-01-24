import re

def validate_input(message):

    is_input_wrong=True
    while is_input_wrong:
        input_msg = input(message)
        if re.match("^[0-9 ]+$", input_msg):
            return input_msg
        else:
            print("Your input is wrong, please correct")
            continue
        

first_input, second_input = validate_input("Input num sequence with space: "), validate_input("Input number: ")

first_input = sorted(list(map(int, first_input.strip().split())))
second_input = int(second_input.strip())
print(first_input, second_input)
print(sorted(first_input))


def binfind(a_list, x, left, right):
    if left > right or len(a_list) == 0:
        return False
    middle = (left + right) // 2
    if a_list[middle] == x:
        return middle
    elif (a_list[middle] < x):
        return binfind(a_list, x, middle + 1, right)
    else:       # a_list[middle] > x
        return binfind(a_list, x, left, middle - 1)

print(binfind(first_input, second_input, 0, len(first_input)-1))

def find_indexes(a_list, x):
    find_x = binfind(a_list, x, 0, len(a_list)-1)
    if find_x == False:
        return "Element wasn't found"
    if find_x in range(0, len(a_list)-1):
        return find_x-1, find_x+1

print(find_indexes(first_input, second_input))