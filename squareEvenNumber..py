#WAP to sum of square of even number
n = int(input("Enter a number: "))
sum_even_squares = 0

for i in range(2, n + 1, 2):
    sum_even_squares += i * i

print("Sum of squares of even numbers up to", n, "is:", sum_even_squares)