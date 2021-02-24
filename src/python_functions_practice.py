def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1 , number_2):
     return  number_1 * number_2 
def divide(number_1 , number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)
def join_string(string_1 , string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(number_1):
    months = ["January","Febuary","March","April","May","June",
    "July","August","September","October","November","December"]
    return months [number_1 - 1]

def number_to_short_month_name(number_1):
    short_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    return short_months [number_1 - 1 ]

def vol_of_cube(side_length):
    return side_length **3

def reverse_string(string_1):
     new_strings = []
     index = len(string_1)
     while index:
        index -= 1                       
        new_strings.append(string_1[index])
     return ''.join(new_strings)