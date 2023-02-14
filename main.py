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

# Implement Bubble Sort
def bubble_sort(unsorted_requirements):
    # Create a copy of the unsorted requirements
    sorted_requirements = unsorted_requirements.copy()
    
    # Take two elements
    for i in range(len(sorted_requirements)):
        for j in range(0, len(sorted_requirements) - i - 1):
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

            # Swap the rows in the dataframe if the second element has more priority
            if user_input == 2:
                sorted_requirements.iloc[[j, j + 1]] = sorted_requirements.iloc[[j + 1, j]]
    
    # Return the sorted requirements
    return sorted_requirements

# Sort the requirements
sorted_requirements = bubble_sort(requirements)

# Write the sorted requirements to a csv file called sorted_requirements.csv
pd.DataFrame(sorted_requirements).to_csv('sorted_requirements.csv', index=False)
