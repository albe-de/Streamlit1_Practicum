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
    response.raise_for_status() 
    csv_content = response.text

    csvfile = StringIO(csv_content)
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    names, descriptions, quantities = [], [], []

    for row in reader:
        if not row: continue
        names.append(row[0])
        quantities.append(row[-1])

        description = ','.join(row[1:-1])
        descriptions.append(description)
    
    return names, descriptions, quantities

names, descriptions, quantities = dumpCSV()
print(names)