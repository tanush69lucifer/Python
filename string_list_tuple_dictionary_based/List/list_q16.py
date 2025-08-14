# getting a sublist from a string
lst=input("Enter elements separated by commas: ").split(",")
start=int(input("Enter the start index: "))
end=int(input("Enter the end index: "))
print("Sublist:", lst[start:end])
