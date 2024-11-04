rows = int(input("Enter the number of rows: "))
current_number = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(current_number, end=" ")
        current_number += 1
    print()
