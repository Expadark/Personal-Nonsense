list1 = []
list2 = []
list3 = []

def another_number(x):
    list1.append(x)

def number_in_list(list_1):
    num_items = 0
    for item in list_1:
        num_items += 1
    return num_items


def find_average(list_1):
    total_value = 0
    for item in list_1:
        total_value += item
    avg = total_value / number_in_list(list_1)
    return avg

def subtract_average(list_1, avg):
    for item in list_1:
        minus_average = item - avg
        list2.append(minus_average)

def square_list(list_1):
    for item in list_1:
        y = item ** 2
        list3.append(y)

def square_root(x):
    y = x ** 0.5
    return y

def population_standard_deviation(list_1):
    subtract_average(list_1,find_average(list_1))
    square_list(list2)
    return square_root(find_average(list3))

def sample_standard_deviation(list_1):
    subtract_average(list_1, find_average(list_1))
    square_list(list2)
    sample_number = number_in_list(list_1) - 1
    total_value = 0
    for item in list3:
        total_value += item
    avg = total_value / sample_number
    return square_root(avg)



print("Okay so basically when it asks 'Add to list?'")
print("You either want to type in a number, or just the letter 'n'")
print("Numbers will be added to the list, and when you type 'n' it will do the math")

more_numbers = True
while more_numbers:
    x = input("Add to list ? ")
    if x == "n":
        p_or_s = input("Type 's' for sample or 'p' for population : ")
        if p_or_s == 'p':
            print(f"Population Standard Deviation is : {population_standard_deviation(list1)}")
        elif p_or_s == "s":
            print(f"Sample Standard Deviation is : {sample_standard_deviation(list1)}")
        more_numbers = False
    else:
        x = int(x)
        another_number(x)
        print(f"Current list is {list1}")