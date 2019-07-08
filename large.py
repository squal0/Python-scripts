def get_algorithm_result(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
        
def prime_number(number):
    if number < 2:
        return False
    for i in range(2,number):
        if(number % i) == 0:
            return False
    return True
