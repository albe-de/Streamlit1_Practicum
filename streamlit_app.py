from io import StringIO
import streamlit as st
import pandas as pd
import requests
import time
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
        self.apiEndpoint = 'https://sheetdb.io/api/v1/tg7nxf1004y8w'
        self.googleSheet = 'https://docs.google.com/spreadsheets/d/1MtMZush8dUvOZ6LxDmX_e8nZ7zY025Chnsn2OkX43MU/edit#gid=0'

    def getData(self):
        response = requests.get(self.apiEndpoint)
        data = response.json()
        df = pd.DataFrame(data)

        return df

    def addData(self, columnName, val):
        df = self.getData()
        if df and columnName in df.columns:
            new_row = {col: '' for col in df.columns}
            new_row[columnName] = val
            response = requests.post(self.apiEndpoint, json={'data': new_row})
            return response.json()
        
        else: return f"Critical ErrorL Column '{columnName}' does not exist."

    def removeData(self, columnName, val):
        df = self.getData()
        if df and columnName in df.columns:
            df = df[df[columnName] != val]
            updated_data = df.to_dict(orient='records')
            response = requests.put(self.apiEndpoint, json={'data': updated_data})
            return response.json()
        
        else: return f"Critical Error: Column '{columnName}' does not exist."

data = dataStore()

st.title("Mohji's Shop")
st.write(
    data.getData('team1')
)

# round 1:
data.addData('team1', '1')
data.addData('team1', '2')
data.addData('team1', '3')