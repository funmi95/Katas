def sum_two_smallest_numbers(numbers):
    ordered_numbers = sorted(numbers)
    answer = ordered_numbers[0] + ordered_numbers[1]
    return answer

sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])

#NOT useful - it was crap
    smallest1 = numbers[0]
    smallest2 = numbers[0]
    answer = 0
    for number in numbers:
        if number < smallest1:
            smallest1 = number
    for number in numbers:
        if number 
    
        
    return smallest


#Fave from others' solutions (very readable)
def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min



sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])
