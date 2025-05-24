from flask import Flask
import pandas as pd

# Replace with the actual gid of your target tab
sheet_gid = '151132530'
sheet_id = '1fnTW9bKVbEuNUCFcXIecflkyrKgiKVABAasd9Z98BiI'

csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}'



app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    # read and store rows of data from the tab called "entry data" in the google sheet to an array and return it as a json response
    df = pd.read_csv(csv_url)
    df.to_csv('entry_results.csv', index=False)
    entry_results = df.to_dict(orient='records')
    return {'entry_results': entry_results}

    
if __name__ == '__main__':
    app.run()# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.