# Automate the Boring Stuff with Python
# Chapter 3 - Functions

# The Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    # Input Validation
    try:
        number = int(input("Enter number:\n"))
        # Iterate function until number == 1
        while number != 1:
             number = collatz(number)
        break
    except ValueError:
        print("Enter a valid integer")
        continue
