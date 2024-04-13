import json
from datetime import datetime, timedelta

# Path to your text file
file_path = '/home/volar/order10twitter.txt'

# Calculate expiration date, set far in the future
future_years = 50  # Years in the future
expiration_date = datetime.now() + timedelta(days=365 * future_years)
expiration_timestamp = int(expiration_date.timestamp())

# Read the file and parse the lines
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file):
        if 'login;password:' in line:
            parts = line.split(':')
            username = parts[0].split(';')[-1].strip()
            password = parts[1].strip()
            email = parts[2].strip()
            ct0 = parts[3].strip()
            auth_token = parts[4].strip()

            # Each cookie info for individual files
            cookies = [
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "auth_token", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": auth_token},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "ct0", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": ct0},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "login", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": username},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "password", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": password},
                {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "mail", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": email}
            ]

            # Create a unique JSON file for each user
            file_name = f'cookie_{username}_{line_number+1}.json'
            with open(file_name, 'w') as json_file:
                json.dump(cookies, json_file, indent=2)

            print(f"JSON file {file_name} has been created.")
