"""""
Un hombre desea saber cuánto dinero se genera por concepto de intereses
en relación la cantidad que tiene en inversión en el banco.
El decidirá reinvertir los intereses siempre y cuando estos no excedan a $7000,
y en ese caso diseña un algoritmo para saber cuánto dinero tendrá
finalmente en su cuenta.
"""
InitialAmount = float(input("enter the initial amount invested: "))
annualInterestRate = float(input("Enter the annual interest rate: "))
timeFrame = float(input("Enter the time period of the investment in years: "))
interests = annualInterestRate * annualInterestRate * timeFrame
if interests> 7000:
    finalAmount = annualInterestRate + interests
    print(f"The final amount in the account is:{finalAmount:.0f}")
else:
    print(f"interest is not reinvested")
