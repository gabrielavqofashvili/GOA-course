def print_odd_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} - even")
        else:
            print(f"{i} - odd")

# Taking input from the user
number = int(input("Enter a number: "))
print("Printing odd/even numbers up to", number)
print_odd_even_numbers(number)