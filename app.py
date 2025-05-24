from flask import Flask
import pandas as pd

google_sheet_url = 'https://docs.google.com/spreadsheets/d/1fnTW9bKVbEuNUCFcXIecflkyrKgiKVABAasd9Z98BiI/edit?usp=sharing'


app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    # read and store rows of data from the tab called "entry data" in the google sheet to an array and return it as a json response
    df = pd.read_csv(google_sheet_url.replace('/edit?usp=sharing', '/gviz/tq?tqx=out:csv'))
    entry_data = df[df['tab'] == 'entry data'].to_dict(orient='records')
    return {'data': entry_data}

    
if __name__ == '__main__':
    app.run()# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.