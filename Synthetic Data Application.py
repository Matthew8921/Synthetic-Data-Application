import csv
import os
import random

csv_files = ["machine-readable-business-employment-data-Jun-2024-quarter.csv"
             "annual-enterprise-survey-2023-financial-year-provisional.csv"]

#Main menu and shows the loops and won't allow you to skip numbers 
def handle_menu_choice(choice, data, file_chosen, has_header, synthetic_data): 
    """Handle the user's menu choice. Returns the updated data and header status."""
    if choice == 1:
        data, file_chosen = load_file() # This will load the csv file and if you load in multiple csv files the variable file_chosen will load and the program will begin 
    elif choice == 2:
        if data is None:
            print("No data loaded. Please load a file first.") # If you do not load your data then any option won't work 
        else:
            has_header = confirmation_for_header(data)

    elif choice == 3:
        if data is None:
            print("Data not loaded. Please load the data first.")
        else:
            display_data(data)
            
    elif choice == 4:
        count_for_ranges(data, has_header)
    elif choice == 5:
        display_ranges(data)
    elif choice == 6:
        data, synthetic_data = roll_data(data)
    elif choice == 7:
        write_file(data)
    elif choice == 8:
        if synthetic_data is None:
            print("No synthetic data avaliable.")
        else:
            check_values(data, synthetic_data)
    elif choice == 9:
        print("Exiting program. Goodbye!")

        return data, file_chosen, has_header, synthetic_data
    else:
        print("Invalid choice. Please try again.")
    return data, file_chosen, has_header, synthetic_data

def display_menu():
    """Display the main menu to the user.""" # Menu display 
    print("\nMain Menu:")
    print("1. Load File")
    print("2. Header Row")
    print("3. Display Read Data")
    print("4. Count For Ranges")
    print("5. Display Ranges")
    print("6. Roll Data")
    print("7. Write File")
    print("8. Check Values")
    print("9. Exit")


def load_file():

    print("\nAvaliable CSV files: ")
    file_number = 1
    for file in csv_files:
        print(f"{file_number}.{file}")
        file_number += 1 #If you put multiple csv files it will number them and when you press 1 it will list the csv files


    try:
        choice = int(input("Choose the file by number: "))
        if 1 <= choice <= len(csv_files):
            file_chosen = csv_files[choice - 1]

            with open(file_chosen, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                data = list(csv_reader)

            if not data:
                print(f"File '{file_chosen}' doesn't exist")
                return None, None

            print(f"File '{file_chosen}' loaded successfully.")
            return data, file_chosen



        else:
            print("Invalid selection. Try again")
    except ValueError:
        print("Invalid. Please enter a number")
    except FileNotFoundError:
        print(f"The file for {file_chosen} could not be found. Please check if the file path is correctr  .") 
    except Exception as e:
        print(f"Error while loading the file: {e}")
    return None, None





def confirmation_for_header(data): # Purpose of the function is to confirm if the first row in data has accurate header information
    if not data:
        print("There's no data to check for headers.")
        return False

    print("\nThe first five rows of your data are:")

    cw = [max(len(str(cell)) for cell in col) for col in zip(*data)] 

    for row in data[:5]:
        row_str = ""

        for cell, width in zip(row, cw):
            str_cell = str(cell)
            ground_cell = str_cell + " " * (width - len(str_cell))
            row_str += ground_cell + " | "

        print(row_str[:-2])


# Ask the user if the header is correct
    while True:
        verify_header = input("\nDoes the first row look like a header? (yes/no): ").strip().lower()
        if verify_header == "yes":
            return True
        elif verify_header == "no":
            return False
        else:
            print("Sorry, I did not get that. Please type yes or no.")
            

    

def display_data(data):
    print("\nDisplaying the first 50 parsed records:\n")

    cw = [max(len(str(cell)) for cell in col) for col in zip(*data)] # Each column will find the max width so that it can show all the cells in that column

    header = "" # Create the header by using the string to align just the exact position so it doesn't look messy when it runs 
    for cell, width in zip(data[0], cw):
        str_cell = str(cell)
        cell_ground = str_cell + " " *(width - len(str_cell))
        header += cell_ground + " | "

    print(header[:-2])
    print("-" * len(header)) # Seperating lines that it looks organized and neat

    for row in data[1:51]: 
        row_str = ""
        for cell, width in zip(row, cw):
            str_cell = str(cell)
            cell_ground = str_cell + " " * (width - len(str_cell)) # This will space out so it will organize the alignment better 
            row_str += cell_ground + " | "
        print(row_str[:-2])

    input("\nPress the ENTER to return to the menu......")




def count_for_ranges(data, has_header):
    if not data:
        print("Data did not load. Load the file")
        return
    if not has_header:
        print("Header not set. Complete the header first")
        return

    print("\nCounting district entries in each column....\n")

    input("\nPress the ENTER to return to the menu.....")


def numeric_only(val):
    try:
        float(val)
        return True
    except ValueError:
        return False




def display_ranges(data):
    if not data:
        print("Data is not loaded. Load it first.")
        return

    print("\nColumn Ranges:")

    row_start = 1 if data and not numeric_only(data[0][0]) else 0 #Start the header row 
    num_columns = len(data[0]) #Get all the columns

    for col_index in range(num_columns): #Make sure the loop goes through each column 
        print(f"\nColumn {col_index + 1}:")
        colval = [row[col_index] for row in data[row_start:]] # Getting all the existing columns and extracting. Changes are made before the row begins 

        count_value = {} #This will count every unique value in the column 
        for value in colval:
            count_value[value] = count_value.get(value, 0) + 1

        nm_val = [v for v in count_value.keys() if numeric_only(v)] #If your csv file is non numeric or is numeric this will differentiate 
        non_nm_val = [v for v in count_value.keys() if not numeric_only(v)]

        sort_num = sorted(nm_val, key=lambda x: float(x)) # I wanted the values to least to greatest 
        sort_non_num = sorted(non_nm_val) # This can sort it alphabetically 

        sort_val = sort_num + sort_non_num #Combine the two

        for value in sort_val:
            print(f"{value}: {count_value[value]}")

    input("\nPress the ENTER to return to the menu......")
    


def roll_data(data):

    if not data:
        print("Data is not loading. Load it first")
        return data, synthetic_data

    try:
        number_of_records = int(input("How many records would you like to generate?: ")) #Ask how many would you like generate
        if number_of_records <= 0: # Give error if it's not a positive number 
            print("Please enter a number greater than 0, or a number")
            return data
    except ValueError:
        print("Invalid. Enter a valid number")
        return data, synthetic_data 


    limit = min(number_of_records, 50) # If user wants more rows it will only display the first 50 but will show anything below

    print(f"\nHere are the first {limit} generated records:\n") #Message if it goes over

    has_header = not numeric_only(data[0][0])
    headers = data[0] if has_header else []
    records = data[1:] if has_header else data


# Generate records with the data provided 
    gen_data = []

    for _ in range(number_of_records):
        new_rec = []
        for col in range(len(records[0])):

            if numeric_only(records[0][col]):
                new_rec.append(random.randint(1,100)) #If data is numeric give me a random number between 1 and 100
            else:
                new_rec.append(random.choice([row[col] for row in records]))
        
        gen_data.append(new_rec)

        

    dis_rec = gen_data[:limit]

    if headers:
        cw = []
        for col in zip(*([headers] + dis_rec)):
            m_len = 0
            for cell in col:
                m_len = max(m_len, len(str(cell)))
            cw.append(m_len)



        header_row = "" #Print the header row and accuratley display organization 
        for col_index in range(len(headers)):
            cell = str(headers[col_index])
            ground = " " *(cw[col_index] - len(cell))
            header_row += cell + ground + " "
        print(header_row)
        print("-" * len(header_row))

    else:

        cw = [] # Get the widths with loops
        for col in zip(*dis_rec):
            m_len = 0
            for cell in col:
                m_len = max(m_len, len(str(cell)))
            cw.append(m_len)

    for row in dis_rec: #Display the rows of the data
        form_row = ""
        for col_index in range(len(row)):
            cell = str(row[col_index])
            ground = " " * (cw[col_index] - len(cell))
            form_row += cell + ground + " "
        print(form_row)

    header_checker = input("\nDoes this look good? If yes, press ENTER.") #Ask the user if its good
    return data, gen_data



def write_file(data):
    if not data:
        print("No data to save. Please generate or load data first.")
        return

    filename = input("Enter the name for the output file (without extension): ").strip() 

    if not filename:
        print("Invalid file name. try agian")
        return

    filename += '.csv'

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            if isinstance(data, list) and data:
                writer.writerows(data)

        print(f"Synthetic data successfully saved to {filename} in current directory.") #Confirmation that the csv file is saved 

    except Exception as e:
        print(f"Error while writing the file: {e}") #Error message if it goes wrong 



def get_column_counts(column_data):
    counts = {} # This will initialize 
    for value in column_data: #Looping will help get the value of each list
        counts[value] = counts.get(value, 0) + 1
    return counts


def check_values(source_data, synthetic_data):

    """Compare the statistical distributions of source and synthetic data and provide total and column-wise scores."""
    if source_data is None or len(source_data) == 0:
        print("No source data loaded. Please load a file first.")
        return
    if synthetic_data is None or len(synthetic_data) == 0:
        print("No synthetic data available. Please generate data first using option 6.")
        return

    try:
        # Ask the user for a margin of error
        margin_of_error = float(input("Enter the margin of error percentage (e.g., 5 for 5%): ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Remove header row if set
    source_data_values = source_data[1:] if isinstance(source_data[0], list) and source_data[0] == source_data[0] else source_data
    synthetic_data_values = synthetic_data

    # Determine the maximum column count
    max_columns = max(len(row) for row in source_data_values)

    # Prepare for comparison
    overall_total_divergence = 0
    overall_total_values = 0
    column_scores = []

    print("\nChecking statistical divergence between source and synthetic data...\n")

    for col_index in range(max_columns):
        # Safely collect column data
        source_column = [row[col_index] for row in source_data_values if col_index < len(row)]
        synthetic_column = [row[col_index] for row in synthetic_data_values if col_index < len(row)]

        if not source_column or not synthetic_column:
            # Skip empty or mismatched columns
            print(f"Skipping column {col_index + 1} due to missing data in source or synthetic data.")
            continue

        # Get counts for each value in the column
        source_counts = get_column_counts(source_column)
        synthetic_counts = get_column_counts(synthetic_column)

        # Normalize counts to percentages
        source_total = sum(source_counts.values())
        synthetic_total = sum(synthetic_counts.values())

        total_divergence = 0
        total_values = 0

        for value in set(source_counts.keys()).union(synthetic_counts.keys()):
            source_percentage = (source_counts.get(value, 0) / source_total) * 100
            synthetic_percentage = (synthetic_counts.get(value, 0) / synthetic_total) * 100
            divergence = abs(source_percentage - synthetic_percentage)

            # Track total divergence for scoring
            total_divergence += divergence
            total_values += 1

        # Calculate average divergence for the column
        average_divergence = total_divergence / total_values if total_values > 0 else 0
        column_scores.append((col_index + 1, average_divergence))

        # Update overall scores
        overall_total_divergence += total_divergence
        overall_total_values += total_values

    # Calculate overall score for the dataset
    overall_score = overall_total_divergence / overall_total_values if overall_total_values > 0 else 0

    # Display results
    print(f"Total Dataset Score: Average Divergence = {overall_score:.2f}%")
    print("\nColumn-Wise Score Breakdown:")
    for col_index, avg_divergence in column_scores:
        status = "<good>" if avg_divergence <= margin_of_error else "<bad>"
        print(f"Column {col_index}: Average Divergence = {avg_divergence:.2f}% {status}")

    input("\nPress ENTER to return to menu...")





def main():
    data = None
    file_chosen = None
    has_header = False
    synthetic_data = None
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 9:
                print("Exiting program")
                break
            data,file_chosen,has_header, synthetic_data = handle_menu_choice(choice, data, file_chosen, has_header, synthetic_data)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
                   
            
    
