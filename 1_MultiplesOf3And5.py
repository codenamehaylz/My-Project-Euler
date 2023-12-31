# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples in 23.
# Find the sum of all multiples of 3 or 5 below 1000.


def multiples_of_3_or_5(num):
    sum = 0
    for num in range(0, num):
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum


print(multiples_of_3_or_5(1000))