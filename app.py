from flask import Flask, jsonify
import pandas as pd

# Replace with the actual gid of your target tab
sheet_gid = '151132530'
sheet_id = '1fnTW9bKVbEuNUCFcXIecflkyrKgiKVABAasd9Z98BiI'

google_sheet_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}'

google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScGJ_XcP0bFe481GweWjf9k55SSGLVwWSoXP4PxKiJlFKGkhQ/viewform?usp=header'

app = Flask(__name__)

@app.route('/')
def index():
    # insert clickable linke to the Google Form and link to entries
    return f"""
    <h1>Welcome to the Entry Results Page</h1>
    <p>Click <a href="{google_form_url}">here</a> to fill out the Google Form.</p>
    <p>Click <a href="/entries">here</a> to view all entries.</p>
    """


@app.route('/entries', methods=['GET'])
def entries():
    # get all active entries (rows) and display just the email addresses using html <h2> tags 
    try:
        df = pd.read_csv(google_sheet_url)
        entry_results = df.to_dict(orient='records')
        emails = [f"<h2>{entry['Email Address']}</h2>" for entry in entry_results if 'Email Address' in entry]
        return ''.join(emails)

    except Exception as e:
        return str(e), 500

@app.route('/api/entryresults', methods=['GET'])
def home():
    try:
        df = pd.read_csv(google_sheet_url)
        entry_results = df.to_dict(orient='records')
        return jsonify({'entry_results': entry_results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
if __name__ == '__main__':
    app.run()# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.