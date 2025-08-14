# 1 
def check_voting_eligibility(age, has_voter_id):
    print((age >= 18 and has_voter_id and "Eligible to vote") or "Not eligible to vote")

# Test the function
check_voting_eligibility(20, True)  # Output: Eligible to vote
check_voting_eligibility(16, True)  # Output: Not eligible to vote

# 2
def check_password_strength(password):
    print((len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and "password" not in password.lower() and "Password is strong") or "Password is weak")

# Test the function
check_password_strength("StrongPass123")  # Output: Password is strong
check_password_strength("pass123")        # Output: Password is weak

# 3
def can_issue_book(overdue_books, library_card_valid):
    print((overdue_books == 0 and library_card_valid and "Book can be issued") or "Cannot issue book")

# Test the function
can_issue_book(0, True)  # Output: Book can be issued
can_issue_book(2, True)  # Output: Cannot issue book

# 4
def atm_withdrawal(balance, atm_working, withdrawal_amount):
    print((balance >= withdrawal_amount and atm_working and "Withdrawal successful") or (balance < withdrawal_amount and "Insufficient balance") or "ATM out of service")

# Test the function
atm_withdrawal(5000, True, 3000)  # Output: Withdrawal successful
atm_withdrawal(1000, True, 2000)  # Output: Insufficient balance

# 5 
def is_leap_year(year):
    print(((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and "Leap year") or "Not a leap year")

# Test the function
is_leap_year(2020)  # Output: Leap year
is_leap_year(1900)  # Output: Not a leap year

# 6
def car_loan_approval(credit_score, job_stable):
    print((credit_score >= 650 and job_stable and "Loan approved") or "Loan not approved")

# Test the function
car_loan_approval(700, True)  # Output: Loan approved
car_loan_approval(600, True)  # Output: Loan not approved

# 7 
def is_divisible_by_3_and_5(number):
    print((number % 3 == 0 and number % 5 == 0 and "Divisible by both 3 and 5") or "Not divisible by both 3 and 5")

# Test the function
is_divisible_by_3_and_5(15)  # Output: Divisible by both 3 and 5
is_divisible_by_3_and_5(10)  # Output: Not divisible by both 3 and 5

# 8
def access_secure_area(access_card, security_clearance):
    print((access_card and security_clearance and "Access granted") or "Access denied")

# Test the function
access_secure_area(True, True)  # Output: Access granted
access_secure_area(True, False)  # Output: Access denied

# 9
def discount_eligibility(is_member, purchase_amount):
    print((is_member or purchase_amount > 100 and "Discount applied") or "No discount")

# Test the function
discount_eligibility(False, 120)  # Output: Discount applied
discount_eligibility(True, 50)    # Output: Discount applied
discount_eligibility(False, 80)   # Output: No discount

#10
def class_attendance(attendance, assignments_submitted):
    print((attendance >= 75 and assignments_submitted and "Allowed to take the exam") or "Not allowed to take the exam")

# Test the function
class_attendance(80, True)  # Output: Allowed to take the exam
class_attendance(70, True)  # Output: Not allowed to take the exam








