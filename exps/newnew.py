def calculate_shares_issued(amount_raised, percentage_ownership):
    shares_issued = (amount_raised / percentage_ownership) * 100
    return shares_issued

def main():
    amount_raised = float(input("Enter the amount to be raised in dollars: "))
    percentage_ownership = float(input("Enter the desired percentage ownership (e.g., 5 for 5%): "))

    shares_issued = calculate_shares_issued(amount_raised, percentage_ownership)
    total_shares = shares_issued / (percentage_ownership / 100)

    print("The number of shares your company needs to issue is:", shares_issued)
    print("The total number of shares your company should have overall is:", total_shares)

if __name__ == "__main__":
    main()
