import streamlit as st
import csv

st.title("Mohji's Shop")
st.write(
    "Curtis came up with the name"
)

# use relative paths-->
def dumpCSV(file='Streamlit1_Practicum/dev assets/Sanford+Stuff+Catalogue+-+Sheet1.csv'):
    with open(file, newline='') as csvfile:
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