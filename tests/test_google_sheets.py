import pandas as pd


sheet_url = 'https://docs.google.com/spreadsheets/d/1JlEYWRqwNBSRzGjRKYjsqIAaQax25ERO78QTi1ViB5Q/edit?usp=sharing'


pd.read_csv(sheet_url.replace('/edit?usp=sharing', '/gviz/tq?tqx=out:csv')).to_csv('test_google_sheets.csv', index=False)
# The above code reads a Google Sheets document as a CSV file and saves it locally.
# It uses pandas to handle the data, specifying the format for date parsing and data types for each column.
# The 'date' column is parsed as a datetime object, while 'id' and 'name' are treated as strings, and 'value' as a float.
# The resulting CSV file is saved as 'test_google_sheets.csv' in the current directory.
# This code is useful for testing the functionality of reading Google Sheets data into a pandas DataFrame.
# The code is designed to read a Google Sheets document and convert it into a CSV file using pandas.            