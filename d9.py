...
9) Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
...
from collections import Counter

input_values = [input().strip() for _ in range(int(input()))]
value_counts = Counter(input_values)

duplicate_count = sum(1 for count in value_counts.values() if count > 1)
unique_values = set(value_counts.keys())

print(f"Duplicate Values: {duplicate_count}")
print(" ".join(sorted(unique_values)) + " ")
