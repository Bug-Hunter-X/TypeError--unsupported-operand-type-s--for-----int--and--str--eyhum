def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle the case where there are no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
print(f"The average of an empty list is: {calculate_average(my_empty_list)}")

my_numbers_with_error = [10, 20, 'a', 40, 50]
print(f"The average of a list with an error is: {calculate_average(my_numbers_with_error)}") #This will correctly return 30