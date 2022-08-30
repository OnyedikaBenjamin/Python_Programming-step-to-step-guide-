loanAmount = eval(input("Enter the loan amount : "))
annualInterestRate = eval(input("Enter the annualInterestRate : "))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input("Enter number of years : "))

monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - (1 / (1 + monthlyInterestRate)**(numberOfYears * 12)))
totalPayment = monthlyPayment * numberOfYears * 12

print("The monthly payment is", int(monthlyPayment))
print("The total payment is", int(totalPayment))
