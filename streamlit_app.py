from io import StringIO
import streamlit as st
import pandas as pd
import requests
import csv

st.title("Mohji's Shop")
st.write(
    "Curtis came up with the name"
)

# use github links to access data-->
csvLocation = 'https://github.com/albe-de/Streamlit1_Practicum/blob/main/dev%20assets/Sanford%2BStuff%2BCatalogue%2B-%2BSheet1.csv'
def dumpCSV(file=csvLocation):
    response = requests.get(file)
    response.raise_for_status()  # Ensure we notice bad responses
    csv_content = response.text

    # Use StringIO to make the string data behave like a file object
    csvfile = StringIO(csv_content)
    
    # Read the CSV data
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    names, descriptions, quantities = [], [], []

    for row in reader:
        if not row:  # Skip empty rows
            continue
        # Assuming the CSV structure: Name, Description, Quantity
        names.append(row[0])
        quantities.append(row[-1])
        
        # Join everything in between as description
        description = ','.join(row[1:-1])
        descriptions.append(description)
    
    return names, descriptions, quantities

# Retrieve and process the data
names, descriptions, quantities = dumpCSV()

# Print results for verification
print("Names:", names)
print("Descriptions:", descriptions)
print("Quantities:", quantities)