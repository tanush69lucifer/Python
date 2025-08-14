# sum of elements in a list
lst=list(map(int, input("Enter numbers separated by commas: ").split(",")))
def sum_list(lst):
    return sum(lst)
print("Sum of elements:", sum_list(lst))
