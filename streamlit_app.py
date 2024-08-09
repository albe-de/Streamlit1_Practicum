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

class dataStore:
    def __init__(self):
        self.api_endpoint = 'https://sheetdb.io/api/v1/tg7nxf1004y8w'
        self.google_sheet = 'https://docs.google.com/spreadsheets/d/1MtMZush8dUvOZ6LxDmX_e8nZ7zY025Chnsn2OkX43MU/edit#gid=0'

    def get_data(self, column_name):
        """Get data for the specified column."""
        response = requests.get(self.api_endpoint)
        data = response.json()
        df = pd.DataFrame(data)
        
        return df

    def add_data(self, column_name, new_value):
        """Add data to the end of the specified column."""
        response = requests.get(self.api_endpoint)
        data = response.json()
        df = pd.DataFrame(data)
        if column_name in df.columns:
            new_row = {col: '' for col in df.columns}
            new_row[column_name] = new_value
            response = requests.post(self.api_endpoint, json={'data': new_row})
            return response.json()
        else:
            return f"Column '{column_name}' does not exist."

    def remove_data(self, column_name, value_to_remove):
        """Remove data from the specified column and shift remaining data up."""
        response = requests.get(self.api_endpoint)
        data = response.json()
        df = pd.DataFrame(data)
        if column_name in df.columns:
            df = df[df[column_name] != value_to_remove]
            updated_data = df.to_dict(orient='records')
            response = requests.put(self.api_endpoint, json={'data': updated_data})
            return response.json()
        else:
            return f"Column '{column_name}' does not exist."

data = dataStore()

st.title("Mohji's Shop")
st.write(
    data.get_data('team1')
)