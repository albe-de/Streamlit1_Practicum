import streamlit as st
import pandas as pd
import csv

st.title("Mohji's Shop")
st.write(
    "Curtis came up with the name"
)

# use github links to access data-->
csvLocation = 'https://github.com/albe-de/Streamlit1_Practicum/blob/main/dev%20assets/Sanford%2BStuff%2BCatalogue%2B-%2BSheet1.csv'
def dumpCSV(file=csvLocation):
    with open(pd.read_csv(file, index_col=0), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        names, descriptions, quantities = [],[],[]
        
        for row in spamreader:
            info = ' '.join(row).split(',')
            quantities.insert(-1, info[-1])
            names.insert(-1, info[0])

            des = ''
            for i in range(1, len(info) - 1): des += info[i]
            descriptions.insert(-1, des)

        return names, descriptions, quantities
    return


names, descriptions, quantities = dumpCSV()
print(names[3])