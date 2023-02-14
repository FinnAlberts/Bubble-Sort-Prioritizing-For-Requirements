import pandas as pd

# Ask user what the delimiter is in the csv file
print("What is the delimiter in the csv file? (; or ,)")
delimiter = input("Enter the delimiter: ")

# Validate input
while delimiter != ";" and delimiter != ",":
    print("\nInvalid input. Please enter ; or ,.")
    delimiter = input("Enter the delimiter: ")

# Read a csv file called requirements.csv using pandas
requirements = pd.read_csv('requirements.csv', sep=delimiter)

# Prioritization function based on the bubble sort algorithm
def prioritize(unsorted_requirements):
    # Create a copy of the unsorted requirements
    sorted_requirements = unsorted_requirements.copy()

    # Initialize a empty dataframe for comparisons. They will be stored as a dictionary of dictionaries
    # E.g. {'requirement1': {'requirement2': True, 'requirement3': False}, 'requirement2': {'requirement1': False, 'requirement3': True}}
    # True means that requirement1 has more priority than requirement2
    comparisons = {}
    for i in range(len(sorted_requirements)):
        comparisons[sorted_requirements['requirement'][i]] = {}
    
    # Take two elements
    for i in range(len(sorted_requirements)):
        # Check if the list is sorted
        done_sorting = True
        for j in range(0, len(sorted_requirements) - i - 1):
            swap = False
            # Check if the two requirements have already been compared
            if sorted_requirements['requirement'][j] in comparisons and sorted_requirements['requirement'][j + 1] in comparisons[sorted_requirements['requirement'][j]]:
                if comparisons[sorted_requirements['requirement'][j]][sorted_requirements['requirement'][j + 1]]:
                    swap = True
                else:
                    swap = False
            elif sorted_requirements['requirement'][j + 1] in comparisons and sorted_requirements['requirement'][j] in comparisons[sorted_requirements['requirement'][j + 1]]:
                if comparisons[sorted_requirements['requirement'][j + 1]][sorted_requirements['requirement'][j]]:
                    swap = False
                else:
                    swap = True
            # If the two requirements have not been compared, ask the user which requirement has more priority
            else:
                counter += 1
                # Ask the user which requirement has more priority
                print("\nWhat requirement does have more priority?\n1)", sorted_requirements['requirement'][j], "\n2)", sorted_requirements['requirement'][j + 1])
                user_input = input("Enter 1 or 2: ")

                # Convert the user input to an integer if it is a number
                if user_input.isdigit():
                    user_input = int(user_input)

                # Validate the user input
                while user_input != 1 and user_input != 2:
                    print("\nInvalid input. Please enter 1 or 2.")
                    user_input = input("Enter 1 or 2: ")

                    # Convert the user input to an integer if it is a number
                    if user_input.isdigit():
                        user_input = int(user_input)

                # If user input is 2, swap the rows in the dataframe
                if user_input == 2:
                    swap = True

            # Swap the rows in the dataframe if the second element has more priority
            if swap == True:
                # Set done_sorting to False because a swap was made, so the list is not sorted
                done_sorting = False

                # Swap the rows
                sorted_requirements.iloc[[j, j + 1]] = sorted_requirements.iloc[[j + 1, j]]

                # Add the comparison to the comparisons dictionary
                comparisons[sorted_requirements['requirement'][j]][sorted_requirements['requirement'][j + 1]] = False
            else: 
                # Add the comparison to the comparisons dictionary
                comparisons[sorted_requirements['requirement'][j]][sorted_requirements['requirement'][j + 1]] = True
        
        # If no swaps were made, the list is sorted
        if done_sorting:
            break

    # Return the sorted requirements
    return sorted_requirements

# Sort the requirements
sorted_requirements = prioritize(requirements)

# Write the sorted requirements to a csv file called sorted_requirements.csv
pd.DataFrame(sorted_requirements).to_csv('sorted_requirements.csv', index=False)
