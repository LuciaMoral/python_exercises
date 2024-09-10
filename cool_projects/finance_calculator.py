
"""
create a monthly income calculator that applies a tax rate 
"""

def calculate_finances(monthly_income: float, tax_rate: float, expenses: float, currency: str) -> None:
    yearly_salary = monthly_income * 12
    monthly_tax = monthly_income * (tax_rate / 100)
    yearly_tax = monthly_tax * 12
    monthly_net_income = monthly_income - monthly_tax
    yearly_net_income = yearly_salary - yearly_tax
    monthly_net_income_final = monthly_net_income - expenses

    
    print("-----------------")
    print(f"Monthly income: {currency} {monthly_income: ,.2f}")
    print(f"Monthly tax rate: {tax_rate: ,.0f}")
    print(f"Montly net income: {currency}{monthly_net_income: ,.2f}")
    print(f"Yearly Salary: {currency}{yearly_salary: ,.2f}")
    print(f"Yearly tax paid: {currency}{yearly_tax: ,.2f}")
    print(f"Yearly net income: {currency}{yearly_net_income: ,.2f}")
    print(f"after your expenses, you are left with a total monthly of {monthly_net_income_final}")
    



def main():
    try: 
        monthly_income = float(input("enter your monthly salary:  "))
        tax_rate =  float(input("enter your tax rate (%): "))
        expenses = float(input("enter your monthly expenses: "))
    except ValueError:
        print("invalid input, please enter number")
        main()

    calculate_finances(monthly_income, tax_rate, expenses, currency="EUR")


if __name__ == "__main__":
    main()