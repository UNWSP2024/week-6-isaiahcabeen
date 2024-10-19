def calculate_tax(total_sales):
    state_tax_rate = 0.05
    county_tax_rate = 0.025
    
    county_tax = total_sales * county_tax_rate
    state_tax = total_sales * state_tax_rate
    total_tax = county_tax + state_tax
    
    return county_tax, state_tax, total_tax

def main():
    total_sales = float(input("Enter the total sales for the month: "))
    
    county_tax, state_tax, total_tax = calculate_tax(total_sales)

    print(f"Amount of county sales tax: {county_tax:.2f}")
    print(f"Amount of state sales tax: {state_tax:.2f}")
    print(f"Total sales tax: {total_tax:.2f}")

if __name__ == '__main__':
    main()
