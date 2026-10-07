print("======================================")
print("       PYTHON PROGRAMS AUDIT")
print("======================================")

# Student Audit
print("\n1. STUDENT PROGRAM")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))

if 0 <= marks <= 100:
    print("Student record is VALID.")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Marks:", marks)
else:
    print("Student record is INVALID. Marks must be between 0 and 100.")


# Fibonacci Audit
print("\n2. FIBONACCI PROGRAM")
n = int(input("Enter number of Fibonacci terms: "))

if n > 0:
    a = 0
    b = 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
else:
    print("Invalid input. Number of terms must be greater than 0.")


# Factorial Audit
print("\n3. FACTORIAL PROGRAM")
num = int(input("Enter a number: "))

if num >= 0:
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "=", factorial)
else:
    print("Factorial is not defined for negative numbers.")


# Armstrong Audit
print("\n4. ARMSTRONG PROGRAM")
num = int(input("Enter a number: "))

if num >= 0:
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")
else:
    print("Please enter a non-negative number.")


# Prime Audit
print("\n5. PRIME PROGRAM")
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")


# Pronic Audit
print("\n6. PRONIC PROGRAM")
num = int(input("Enter a number: "))

is_pronic = False

for i in range(num + 1):
    if i * (i + 1) == num:
        is_pronic = True
        break

if is_pronic:
    print(num, "is a Pronic number.")
else:
    print(num, "is not a Pronic number.")


print("\n======================================")
print("          AUDIT COMPLETED")
print("======================================")
