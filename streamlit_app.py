# from streamlit_gsheets import GSheetsConnection
from io import StringIO
import streamlit as st
import pandas as pd
import requests
import csv

# third party meathods for exess site usage
class exessMeathods():
    def __init__(self): pass
    def dumpCSV(self, file='https://github.com/albe-de/Streamlit1_Practicum/blob/main/dev%20assets/Sanford%2BStuff%2BCatalogue%2B-%2BSheet1.csv'):
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

st.title("Mohji's Shop")
st.write(
    "Curtis came up with the name"
)

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")