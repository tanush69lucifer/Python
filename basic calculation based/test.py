n = int(input("Enter the number of rows (n > 0): "))
current_number = 1
for i in range(1, n + 2):
    for j in range(i):
        print(current_number, end=' ')
        current_number += 1
    print() 