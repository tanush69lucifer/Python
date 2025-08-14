#1
username = "admin"
password = "1234"
is_valid = (username == "admin" and len(password) >= 4) or (len(username) < 5)
#2
cpu_available = 60 # in percentage
memory_available = 2048 # in MB
allocate_resource = (cpu_available > 50 and memory_available > 2000) or memory_available == 4096

#3
attempts = 3
locked = False
login_success = (attempts < 5 or not locked) and (attempts > 0)

#4
in_stock = 15
on_hold = 10
can_purchase = (in_stock > 5 or on_hold < 5) and in_stock > 0

#5
in_stock = 15
on_hold = 10
can_purchase = (in_stock > 5 or on_hold < 5) and in_stock > 0

#6
is_member = True
purchase_amount = 120
eligible_for_discount = (is_member and purchase_amount >= 100) or purchase_amount > 150

#7
is_online = True
battery_level = 50
can_update = (is_online and battery_level > 40) or battery_level > 80

#8
has_passport = True
has_visa = False
travel_allowed = (has_passport and has_visa) or not has_visa

#9
attendance = 75
assignments_submitted = True
exam_eligible = (attendance >= 75 and assignments_submitted) or attendance > 80

#10
has_permission = False
is_owner = True
access_file = (has_permission or is_owner) and not has_permission

#11
payment_processed = True
stock_remaining = 3
purchase_successful = (payment_processed and stock_remaining > 0) or stock_remaining > 5

#12
is_complete = False
has_photo = True
form_accepted = (is_complete and has_photo) or not is_complete

#13
cpu_usage = 85
memory_usage = 90
server_healthy = (cpu_usage < 80 or memory_usage < 85) and (cpu_usage < 90 or memory_usage < 95)

#14
credit_score = 700
income = 45000
loan_approved = (credit_score >= 650 and income > 40000) or income > 60000

#15
age = 45
medical_checkup = False
eligible_for_insurance = (age < 50 or medical_checkup) and age > 30

#16
is_weekend = True
low_traffic = False
schedule_maintenance = (is_weekend or low_traffic) and not low_traffic

#17
password_correct = True
otp_verified = False
mfa_successful = password_correct and (otp_verified or not otp_verified)

 #18
experience_years = 5
has_recommendation = False
promotion_approved = (experience_years > 3 or has_recommendation) and not has_recommendation

#19
agents_available = True
queue_length = 5
can_join_chat = agents_available or (queue_length < 10 and not agents_available)
 
#20
items_in_cart = 4
logged_in = False
checkout_possible = (items_in_cart > 0 and logged_in) or (not logged_in and items_in_cart > 2)

