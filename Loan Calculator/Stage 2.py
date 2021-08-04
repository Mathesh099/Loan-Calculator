print("Enter the loan principal:")
loan_principle = int(input())
print("""what do you want to calculate? 
type 'm' - for count of months,
type 'p' - for monthly payment""")
type = input()
if type == "p":
    print("Enter number of months:")
    months = int(input())
    if (months % 2) == 0:
        payment = int(round(loan_principle // months))
        print("Your monthly payment = " + str(payment))
    else:
        payment = int(round(loan_principle // months)) + 1
        last_payment = loan_principle - (months - 1) * payment
        print("Your monthly payment = " + str(payment) + " and the last payment = " + str(last_payment))
elif type == "m":
    print("Enter monthly payment:")
    payment = int(input())
    month = int(round(loan_principle / payment))
    if month > 1:
        print("It will takes " + str(month) + " months to repay the loan")
    else:
        print("It will takes " + str(month) + " month to repay the loan")
