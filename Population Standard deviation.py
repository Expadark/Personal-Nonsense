list1 = []
list2 = []
list3 = []

def another_number(x):
    list1.append(x)

def find_average(list_1):
    num_items = 0
    for item in list_1:
        num_items += 1
    total_value = 0
    for item in list_1:
        total_value += item
    avg = total_value / num_items
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
    list2 = []
    list3 = []
    subtract_average(list_1,find_average(list_1))
    square_list(list2)
    done = square_root(find_average(list2))
    return done

print("Okay so basically when it asks 'Add to list?'")
print("You either want to type in a number, or just the letter 'n'")
print("Numbers will be added to the list, and when you type 'n' it will do the math")

more_numbers = True
while more_numbers:
    x = input("Add to list ? ")
    if x == "n":
        print(f"Current list is {list1}")
        find_average(list1)
        subtract_average(list1, find_average(list1))
        square_list(list2)
        average_of_squared_differences = find_average(list3)
        print(f"Population standard deviaiton is : {square_root(average_of_squared_differences)}")
        input("")
        # population_standard_deviation(list1)
        more_numbers = False
    else:
        x = int(x)
        another_number(x)
        print(f"Current list is {list1}")

