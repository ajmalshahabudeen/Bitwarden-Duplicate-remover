import pandas as pd
df = pd.read_csv('bitwarden.csv', usecols=['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'login_uri', 'login_username', 'login_password', 'login_totp' ]).drop_duplicates(keep='first').reset_index()
file_name = "bitwarden_deduped.csv"
df.to_csv(file_name, index=False) # you don't need to set sep in this because to_csv makes it comma delimited.