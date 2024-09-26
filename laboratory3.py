def loan_eligibility():
    
    print("Welcome to the Loan Eligibility Checker!")
    
   
    try:
        salary = float(input("Please enter your monthly salary: "))
    except ValueError:
        print("Invalid input! Please enter a valid number for your salary.")
        return
    
   
    if salary < 30000:
        print("Sorry, your salary is too low to qualify for a loan.")
        return
    
  
    try:
        loan_amount = float(input("Please enter the loan amount you want to request: "))
    except ValueError:
        print("Invalid input! Please enter a valid number for the loan amount.")
        return
    
    
    if loan_amount > 10 * salary:
        print("Sorry, the loan amount you requested is too high.")
        return
    
    
    try:
        months = int(input("Congratulations! Your loan is approved.\nHow many months do you want to pay the loan over? "))
    except ValueError:
        print("Invalid input! Please enter a valid number of months.")
        return
    
  
    total_with_interest = loan_amount * 1.10
    
    print(f"Loan amount approved: {loan_amount:.2f}")
    print(f"Loan amount with 10% interest: {total_with_interest:.2f}")
    print(f"You chose to pay over {months} months.")
    print(f"Monthly payment: {total_with_interest / months:.2f}")
    print("Thank you for using the Loan Eligibility Checker!")


loan_eligibility()
