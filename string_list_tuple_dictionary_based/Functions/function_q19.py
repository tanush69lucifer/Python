# list to string
lst=input("Enter elements separated by commas: ").split(",")
def list_to_string(lst):
    return ''.join(lst)
print("Converted string:", list_to_string(lst))
