#!/usr/bin/python3
for i in range(10):  # Outer loop for the first digit (0 to 9)
    for j in range(i + 1, 10):  # Inner loop for the second digit (i+1 to 9)
        if i != j:  # Ensure that the two digits are different
            if i == 8 and j == 9:  # Check for the last combination
                print(f"{i}{j}")
            else:
                print(f"{i}{j}", end=", ")
