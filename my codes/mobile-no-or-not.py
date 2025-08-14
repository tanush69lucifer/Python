# Check if the entered number is a mobile number
n = int(input('Enter number: '))
c = 0 #counts the digits
while n > 0: #stores the number for later use
    n = n // 10
    c += 1
if c == 10: #checks if the number is mobile number or not
    print('Number is a mobile number')
else:
    print('Not a mobile number')
