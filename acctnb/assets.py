def calculate_total_assets(current_assets, non_current_assets):
    return current_assets + non_current_assets

def calculate_total_liabilities(current_liabilities, non_current_liabilities):
    return current_liabilities + non_current_liabilities

def calculate_equity(total_assets, total_liabilities, contributed_capital, retained_earnings):
    return total_assets - total_liabilities  # Or Equity = Contributed Capital + Retained Earnings

def main():
    # Taking user inputs
    current_assets = float(input("Enter the value of current assets: $"))
    non_current_assets = float(input("Enter the value of non-current assets: $"))
    current_liabilities = float(input("Enter the value of current liabilities: $"))
    non_current_liabilities = float(input("Enter the value of non-current liabilities: $"))
    contributed_capital = float(input("Enter the value of contributed capital: $"))
    retained_earnings = float(input("Enter the value of retained earnings: $"))

    # Calculating Total Assets, Total Liabilities, and Equity
    total_assets = calculate_total_assets(current_assets, non_current_assets)
    total_liabilities = calculate_total_liabilities(current_liabilities, non_current_liabilities)
    equity = calculate_equity(total_assets, total_liabilities, contributed_capital, retained_earnings)

    # Displaying the results
    print("\nBalance Sheet Formulas:")
    print(f"Total Assets = Current Assets + Non-Current Assets: ${total_assets:.2f}")
    print(f"Total Liabilities = Current Liabilities + Non-Current Liabilities: ${total_liabilities:.2f}")
    print(f"Equity = Total Assets - Total Liabilities: ${equity:.2f} (or Equity = Contributed Capital + Retained Earnings)")

if __name__ == "__main__":
    main()
