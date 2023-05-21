# Bitwarden-Duplicate-remover

Steps:
-----
1. Export from Bitwarden and Rename

- First we are going to export our Bitwarden Vault to a CSV. This can be done by opening           Bitwarden and going to —> File —> Export Vault.
- Select.CSV when it asks for file format.
- Enter your password and download the file.
- Make a copy of the the exported .CSV file and name it to bitwarden.csv.
2. Download the Python Script and Configure Dependenices
3. Run the script!

Simply run the script by navigating to the directory where you downloaded it and run python duplicatefinder.py.
4. Re-Upload Bitwarden Vault

- After the script is run there should be a file called bitwarden_deduped.csv.
- Open up this CSV file in the editor of your choice and check to make sure your important         logins, secure notes, etc are still present and not duplicated.
- If everything looks good it is time to re-upload.
- Navigate to your Bitwarden Webvault (typically, Bitwarden Web Vault).
- Verify one last time that all modfications made by the script are valid and that you are not     missing any important passwords, secure notes, etc.
- Click Settings at the top of the screen and then scroll to the bottom.
- Select Purge Vault, within the “Danger Zone” area at the bottom of the page.
- Select Purge Vault
- Navigate to the top of the page and select “Tools”
- Select Import Data
- Select the CSV file type and upload bitwarden_deduped.csv
- Select Import Data

Congratulations!
----------------
All of your logins and notes should now be de-duplicated and should sync across your devices shortly! Hopefully this saves you some time so you can get back to doing what you do best!
