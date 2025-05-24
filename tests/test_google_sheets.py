import pandas as pd

# Replace with the actual gid of your target tab
sheet_gid = '151132530'
sheet_id = '1fnTW9bKVbEuNUCFcXIecflkyrKgiKVABAasd9Z98BiI'

csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}'

df = pd.read_csv(csv_url)
df.to_csv('entry_results.csv', index=False)

tab_records = df.to_dict(orient='records')
print(tab_records)  # Print the records to verify the data