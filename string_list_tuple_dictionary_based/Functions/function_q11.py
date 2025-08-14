# product of all element in a list
lst=list(map(int, input("Enter numbers separated by commas: ").split(",")))
def product_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
print("Product of elements:", product_list(lst))
