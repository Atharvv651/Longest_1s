def longest_consecutive_ones(n):
    binary_representation = bin(n)[2:]
    max_count = 0
    current_count = 0

    for bit in binary_representation:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

number = int(input("Enter a number: "))
result = longest_consecutive_ones(number)
print("The longest consecutive 1's is:", result)
