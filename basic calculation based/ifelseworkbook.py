# 1 ticket price
def calculate_ticket_price(age, ticket_price, is_3d_movie):
    if age < 12:
        ticket_price *= 0.5
    elif age >= 60:
        ticket_price *= 0.7
    
    if is_3d_movie:
        ticket_price += 5
    
    return ticket_price
# 2 checking fraud
def check_fraud(account_balance, transaction_amount, transaction_time):
    if transaction_amount > 0.7 * account_balance or transaction_time < "06:00" or transaction_time > "22:00":
        return "Transaction flagged as suspicious"
    else:
        return "Transaction is safe"
# 3 discount calculation
def calculate_discount(purchase_amount, is_premium_member):
    if purchase_amount > 200:
        discount = 0.15
    elif 100 <= purchase_amount <= 200:
        discount = 0.10
    else:
        discount = 0

    if is_premium_member:
        discount += 0.05
    
    total_amount = purchase_amount * (1 - discount)
    return total_amount
 # 4 car insurance
def calculate_premium(car_age, owner_age, no_accidents):
    if car_age < 5:
        base_premium = 500
    elif car_age <= 10:
        base_premium = 800
    else:
        base_premium = 1200
    
    if owner_age < 25:
        base_premium *= 1.2
    
    if no_accidents:
        base_premium *= 0.9
    
    return base_premium
# 5 shopping bill
def calculate_bill(units_consumed):
    if units_consumed <= 100:
        bill = units_consumed * 0.5
    elif units_consumed <= 200:
        bill = 100 * 0.5 + (units_consumed - 100) * 0.75
    else:
        bill = 100 * 0.5 + 100 * 0.75 + (units_consumed - 200) * 1.2
    
    if bill > 300:
        bill *= 1.15
    
    return bill
# 6 shipping fee 
def calculate_shipping_fee(destination, weight):
    fee = 0
    if destination == "international":
        fee += 30
    
    if weight > 10:
        fee += (weight - 10) * 5
    
    return fee
# 7 graduation eligibilty
def check_graduation_eligibility(gpa, credits, final_exam_passed):
    if gpa >= 2.5 and credits >= 120:
        if gpa < 3.0 and not final_exam_passed:
            return "Not eligible for graduation"
        else:
            return "Eligible for graduation"
    else:
        return "Not eligible for graduation"
# 8 tax filling status
def determine_tax_filing_status(married, has_dependents):
    if married:
        return "Married"
    elif has_dependents:
        return "Head of Household"
    else:
        return "Single"
# 9 payment plan
def determine_repayment_plan(loan_amount, annual_income):
    if loan_amount < 50000:
        years = 5
    elif loan_amount <= 100000:
        years = 10
    else:
        years = 15
    
    if annual_income < 30000:
        years += 2
    
    return years
# 10 upgrade eligibility 
def check_upgrade_eligibility(points, is_overbooked, is_frequent_flyer):
    if is_frequent_flyer and is_overbooked:
        required_points = 700
    elif is_frequent_flyer:
        required_points = 900
    elif is_overbooked:
        required_points = 800
    else:
        required_points = 1000
    
    if points >= required_points:
        return "Eligible for upgrade"
    else:
       return "Not eligible for upgrade"

