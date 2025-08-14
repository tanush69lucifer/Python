# Check Voting Eligibility
# Input section
age = int(input("Enter your age: "))
has_voter_id = input("Do you have a voter ID? (Yes/No): ").strip().lower()
# Eligibility check
if age >= 18 and has_voter_id == "yes":
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# input section ithout ifelse 
age = int(input("enter your age ")) 
voter_id = input(" you have voter id Yes/No ")
# logic Section 
out = age >= 18  and voter_id == 'Yes'
x=out*"you are eligile for voting"+(1-out)*"you are not eligible for voting"
print(x)
# Display Section 

age=int(input(""))
voter_id=input("has voter id y/n").strip().lower()
if age>=18 and voter_id=="yes":
    print("")
else:
    print("")
