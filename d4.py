...
4) Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
...
values = set(map(int, input().split()))
element_to_delete = int(input())

if element_to_delete in values:
    values.remove(element_to_delete)
    print(" ".join(map(str, sorted(values))) + " ")
else:
    print("Given value is not present in the set list.")
