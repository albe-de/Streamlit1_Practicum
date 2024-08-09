from io import StringIO
import streamlit as st
import pandas as pd
import requests
import time
import csv

# third party meathods for exess site usage
@st.cache_data(show_spinner=False)
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

        return data

    def setData(self, newData):
        if not isinstance(newData, dict):
            raise ValueError("newData must be a dictionary in the format {'team': ['item1', 'item2']}")
        
        response = requests.put(self.apiEndpoint, json=newData)
        print(response.status_code)  # Log status code
        print(response.json())       # Log response JSON

    def addData(self, team, item):
        data = self.getData()
        if team in data:  data[team].append(item)
        else: data[team] = [item]

        response = requests.put(self.apiEndpoint, json=data)
        # return response.json()

ds = dataStore()
new_data = {
    'team1': ['item1', 'item2', 'item4'],
    'team2': ['item3', 'item5'],
    'team3': ['item6']
}
if st.button('Click Me'):
    ds.setData(new_data)

st.title("Mohji's Shop")
# st.write(f'{response}')