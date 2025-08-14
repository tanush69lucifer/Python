mj = 0  # Count of minors (age <= 18)
mn = 0  # Count of non-minors (age > 18)
c = 1

while c <= 10:  # Loop for 10 people
    name = input('Enter name of person {}: '.format(c))
    age = int(input('Enter age of {}: '.format(name)))
    
    if age <= 18:
        mj += 1  # Increment minor count
    else:
        mn += 1  # Increment non-minor count
    
    c += 1  # Increment counter

# Output the results
print("Number of minors (age <= 18):", mj)
print("Number of adults (age > 18):", mn)
#format() allows you to insert the counter c or the person's name into the input into promptf


