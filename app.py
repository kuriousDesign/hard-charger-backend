from flask import Flask, jsonify
import pandas as pd

# Replace with the actual gid of your target tab
sheet_gid = '151132530'
sheet_id = '1fnTW9bKVbEuNUCFcXIecflkyrKgiKVABAasd9Z98BiI'

csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}'



app = Flask(__name__)
@app.route('/api/entryresults', methods=['GET'])
def home():
    try:
        df = pd.read_csv(csv_url)
        entry_results = df.to_dict(orient='records')
        return jsonify({'entry_results': entry_results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
if __name__ == '__main__':
    app.run()# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.