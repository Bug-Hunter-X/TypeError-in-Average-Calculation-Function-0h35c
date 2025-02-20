def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage with error handling
data = [10, 20, 30, 40, 'abc']
result = calculate_average(data)
print(f"The average is: {result}")
data2 = [10,20,30,40]
result2 = calculate_average(data2)
print(f"The average is: {result2}")
