#first if else xample 
'''a=5
if a>1 :
    print("number is greater than 1")
else:
    print("number is not greater than 1") 
#2 
n=int(input("enter value of n : "))
if n%2==0 :
    print("even number") 
else:
     print("odd number")
# 3
r=int(input("enter no. of runs: "))
if r%100==0 and r>300:  print(f'{r // 100}th Century')
elif r>=300:   print("triple century")
elif r>=200: print("double century")
elif r>=100: print("century")
elif r>=50 : print("half century")
else :        print("no century")'''
from typing import Literal
def check_fraud(account_balance: float, transaction_amount: float, transaction_time: str) -> Literal["Transaction flagged as suspicious", "Transaction is safe"]:
    if transaction_amount > 0.7 * account_balance or transaction_time < "06:00" or transaction_time > "22:00":
        return "Transaction flagged as suspicious"
    else:
        return "Transaction is safe"

print(check_fraud(1000.0, 800.0, "05:30"))  
print(check_fraud(1000.0, 500.0, "10:00"))  
print(check_fraud(1000.0, 500.0, "23:00")) 

