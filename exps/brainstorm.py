import datetime

def calculate_ownership(total_investment, percentage_owned):
    total_ownership = 100
    remaining_ownership = total_ownership - percentage_owned
    investor_ownership = (percentage_owned / total_ownership) * total_investment
    return investor_ownership, percentage_owned

def save_results_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    total_investment = float(input("Enter the total investment amount: $"))
    percentage_owned = float(input("Enter the percentage of the company owned by the investors: "))
    total_investors = int(input("Enter the total number of investors: "))

    # Define evaluation milestones
    milestones = [1, 5, 10, 50, 100, 250, 500, 1000, 5000, 10000]  # In millions

    output_content = ""

    # Calculate ownership stake for each evaluation milestone
    for milestone in milestones:
        milestone_evaluation = milestone * 1e6  # Convert to millions
        milestone_investment = milestone_evaluation - total_investment
        new_total_investment = total_investment + milestone_investment
        new_percentage_owned = (percentage_owned * total_investment + milestone_investment) / new_total_investment * 100
        investor_ownership, _ = calculate_ownership(new_total_investment, new_percentage_owned)
        output_content += f"\nFor evaluation milestone of ${milestone} million:\n"
        output_content += "Average amount owed to each investor: $" + str(new_total_investment / total_investors + investor_ownership) + "\n"
        output_content += "Percentage of ownership for each investor: " + str(new_percentage_owned) + "%\n"
        overall_value = milestone_evaluation / (new_percentage_owned / 100)
        output_content += "Value of the overall company (100%): $" + str(overall_value) + "\n"
        stake_per_investor = new_percentage_owned / total_investors
        output_content += "Stake in the company for each investor: " + str(stake_per_investor) + "%\n"

    # Generate timestamp for filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"results_{timestamp}.txt"

    # Save results to the file
    save_results_to_file(filename, output_content)

if __name__ == "__main__":
    main()
