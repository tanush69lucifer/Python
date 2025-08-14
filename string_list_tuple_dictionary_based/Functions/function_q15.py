# smallest element in a list
lst=list(map(int, input("Enter a list of numbers separated by commas: ").split(",")))
def smallest_element(lst):
    return min(lst)
print("Smallest element:", smallest_element(lst))
