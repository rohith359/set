...
2) Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
...
input_values = input().split()
unique_values = set(map(int, input_values))
sorted_values = sorted(unique_values)
print(" ".join(map(str, sorted_values)))

