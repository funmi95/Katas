def digital_root(n):
    sum_of_digits = 0
    more_than_one_digit = True

    while more_than_one_digit == True:
        for digit in str(n):
            sum_of_digits += int(digit) 

        if sum_of_digits > 9:
            n=sum_of_digits
            sum_of_digits = 0
        elif sum_of_digits <= 9 :
            more_than_one_digit = False

    return(sum_of_digits)

    
digital_root(942) #should be 6

#Easier way to do mine
def digital_root(n):
    j = 0
    while n > 9:
        for i in str(n):
            j += int(i)
        n = j
        j = 0
    return n