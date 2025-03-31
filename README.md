CSV Data Processing Tool


Overview
This Python-based CLI tool allows users to load, analyze, and manipulate CSV files efficiently. It provides features such as loading multiple CSV files, displaying data, generating synthetic data, and comparing statistical distributions.

Features
Load CSV Files: Supports loading and handling multiple CSV files.

Header Detection: Allows users to confirm if the first row is a header.

Data Display: View the first 50 records in a structured format.

Count Ranges: Analyze column value distributions.

Generate Synthetic Data: Create randomized synthetic data based on existing values.

Save Processed Data: Export manipulated data to a new CSV file.

Statistical Comparison: Compare source and synthetic data distributions.

Prerequisites
Python 3.x

Required library: None (uses built-in Python modules)

Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-repo/csv-data-tool.git  
Navigate to the project directory:

bash
Copy
Edit
cd csv-data-tool  
Run the script:

bash
Copy
Edit
python main.py  
Usage
Upon running the script, a menu appears with the following options:

Load File – Select a CSV file to process.

Header Row – Confirm whether the first row is a header.

Display Read Data – View the first 50 records.

Count For Ranges – Analyze column value distributions.

Display Ranges – Show column-wise value counts.

Roll Data – Generate synthetic data.

Write File – Save processed data to a CSV file.

Check Values – Compare source and synthetic data.

Exit – Close the program.

Error Handling
Prevents invalid menu selections.

Handles missing or corrupt CSV files.

Ensures numerical data is processed correctly.

Future Enhancements
Support for larger datasets with Pandas integration.

Additional data visualization features.

GUI version for better user experience.

License
This project is licensed under the MIT License.
