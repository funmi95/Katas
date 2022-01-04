def sum_dig_pow(a, b):
    Eureka = []
    for number in range(a,b+1):
        number_as_string = str(number)
        sum = 0
        for index, i in enumerate (number_as_string):
            n = int(i) ** (index+1)
            sum +=n
        if sum == number:
            Eureka.append(number)
    
    return Eureka

sum_dig_pow(9, 1676)

list(range(1,10))

a = list(str(1676))
sum = 0
for index, i in enumerate(a):
    n = int(i) ** (index+1)
    sum +=n
sum
