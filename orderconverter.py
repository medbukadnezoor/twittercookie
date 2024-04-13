import json
import os
from datetime import datetime, timedelta

# Ask for the path to the text file
file_path = input("Enter the path to the text file: ")

# Set the directory for cookies
directory = 'cookies'
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' was created.")

# Check for .gitignore in the cookies directory
gitignore_path = os.path.join(directory, '.gitignore')
if not os.path.isfile(gitignore_path):
    with open(gitignore_path, 'w') as gitignore:
        gitignore.write('*\n!.gitignore')
    print(f".gitignore file created in {directory}")

# Calculate expiration date, set far in the future
future_years = 1  # Years in the future
expiration_date = datetime.now() + timedelta(days=365 * future_years)
expiration_timestamp = int(expiration_date.timestamp())

# Counter for file numbering
file_number = 1

# Read the file and parse the lines
with open(file_path, 'r') as file:
    for line in file:
        if 'login;password:' in line:
            # Extract the fields from each line
            parts = line.strip().split(':')
            username = parts[1].strip()
            password = parts[2].strip()
            email = parts[3].strip()
            ct0 = parts[4].strip()
            auth_token = parts[5].strip()

            # Prepare the cookies data structure
            cookies = [
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "auth_token", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": auth_token},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "ct0", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": ct0},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "login", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": username},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "password", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": password},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "mail", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": email}
            ]

            # Create a unique JSON file for each user
            file_name = f'{directory}/{username}_cookie_{file_number}.json'
            with open(file_name, 'w') as json_file:
                json.dump(cookies, json_file, indent=2)

            print(f"JSON file {file_name} has been created.")
            file_number += 1  # Increment the file number for the next file
