from flask import Flask, jsonify
from flask_apscheduler import APScheduler
import pandas as pd
import time

# Replace with the actual gid of your target tab
gid_entry_results = '151132530'
gid_a_finish = '1647052748'
gid_a_starting = '589664026'
gid_b_finish = '2016018792'
gid_b_starting = '1546972296'

sheet_id = '1fnTW9bKVbEuNUCFcXIecflkyrKgiKVABAasd9Z98BiI'


def tab_url(gid):
    return f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}'

google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScGJ_XcP0bFe481GweWjf9k55SSGLVwWSoXP4PxKiJlFKGkhQ/viewform?usp=header'

app = Flask(__name__)

entry_results = []  # Global variable to store entry results
race_results = []

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
        emails = [f"<h2>email address: {entry['Email Address']} --> score: {entry['Total']}</h2>" for entry in entry_results if 'Email Address' in entry]
        return ''.join(emails)

    except Exception as e:
        return str(e), 500

@app.route('/api/entryresults', methods=['GET'])
def home():
    try:
        return jsonify({'entry_results': entry_results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/raceresults', methods=['GET'])
def provide_race_results():
    return jsonify(race_results)


def get_race_results():
    global race_results
    try:
        df_finish = pd.read_csv(tab_url(gid_a_finish))
        df_starting = pd.read_csv(tab_url(gid_a_starting))
        results = df_finish.to_dict(orient='records')
        # Filter out rows where
    except Exception as e:
        print(f"[ERROR] Failed to fetch sheet: {e}")


def update_entry_results():
    global entry_results
    try:
        prev_len = len(entry_results)
        df = pd.read_csv(tab_url(gid_entry_results))
        entry_results = df.to_dict(orient='records')
        if len(entry_results) != prev_len:
            print(f"[INFO] Entry results updated: {prev_len} -> {len(entry_results)} entries.")
    except Exception as e:
        print(f"[ERROR] Failed to fetch sheet: {e}")


scheduler = APScheduler()

if __name__ == '__main__':
    #update_entry_results()  # Optional: pre-fill data before first request
    scheduler.add_job(id='UpdateEntryResults', func=update_entry_results, trigger='interval', seconds=15)
    scheduler.init_app(app)
    scheduler.start()
    app.run()# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.