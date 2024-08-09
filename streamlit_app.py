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

    # returns raw, unfiltered data
    def getData(self, format=False):
        response = requests.get(self.apiEndpoint)
        data = response.json()

        if not format: return self.formatData(data)
        result = {}

        for d in data:
            # for key, value in d.items():
            for key in range(len(d)):
                if key not in result: result[key] = []
                result[key].append(d[key])
                
        return result


ds = dataStore()
data = ds.getData(False)

st.title("Mohji's Shop")

if st.button('Click Me'):
    st.write(data)
