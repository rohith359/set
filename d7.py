...
5
7) Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
...
values = set(map(int, input().split()))

maximum_value = max(values)
minimum_value = min(values)

print(f"Maximum: {maximum_value}")
print(f"Minimum: {minimum_value}")
