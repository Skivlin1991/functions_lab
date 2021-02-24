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
    months = ["Unknown","January","Febuary","March","April","May","June",
    "July","August","September","October","November","December"]
    return months [number_1]

def number_to_short_month_name(number_1):
    short_months = ["Unknown","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    return short_months [number_1]
    
