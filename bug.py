def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
print(f"The average of an empty list is: {calculate_average(my_empty_list)}") # This will correctly return 0

#Example of the bug
my_numbers_with_error = [10, 20, 'a', 40, 50] #Adding a string to the list
#This will throw an error because you can't sum string with integer
print(f"The average of a list with an error is: {calculate_average(my_numbers_with_error)}")