n = int(input("Enter the number:"))
if n > 1:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            print(n, "is not prime number")
            print(i, "times", n // i, "is", n)
            break

        else:
            print(n, "is prime number")

else:
    print(n, "is not prime number")
