from flask import Flask, render_template
from flask_socketio import SocketIO, emit
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

class DataStore:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(self.app)

        self.data = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": []}

        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.socketio.on('get_data')
        def handle_get_data():
            emit('data_response', self.data)

        @self.socketio.on('update_data')
        def handle_update_data(new_data):
            self.data.update(new_data)
            emit('data_response', self.data, broadcast=True)

if __name__ == '__main__':
    store = DataStore()
    store.socketio.run(store.app, debug=True)


st.title("Mohji's Shop")
st.write(
    "Curtis came up with the name"
)