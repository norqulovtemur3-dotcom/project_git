def calculate_area(*radius):
    for pi in radius:
        if pi >= 10:
            print(pi % 2 == 0)
        else:
            print(pi % 3 == 0)

calculate_area(23, 2, 3, 4, 12, 14)
print("Hello from Teacher")


print("hello from local branch")