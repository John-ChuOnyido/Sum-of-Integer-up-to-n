def sum_integer(expect):
    number = 1
    sum = 0
    while number<expect+1:
        sum += number
        number += 1
    return sum
#collecting data from the user input
expect = int(input("please input the number you want to sum: "))
sum_integer(expect)
