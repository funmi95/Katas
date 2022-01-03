def narcissistic(value):
    value_as_string = str(value)
    number_of_digits = len(value_as_string)
    digit_multipled = 0
    for digit in value_as_string:
        n = int(digit)**number_of_digits
        digit_multipled += n

    if digit_multipled == value:
        return True

    else:
        return False


narcissistic(153)
narcissistic(1652)


#Favourite from other's solutions
def narcissistic( value ):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)