import json
import os
import sys  # Import sys to handle command-line arguments
from datetime import datetime, timedelta

def process_data(file_path):
    directory = 'cookies'
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")

    gitignore_path = os.path.join(directory, '.gitignore')
    if not os.path.isfile(gitignore_path):
        with open(gitignore_path, 'w') as gitignore:
            gitignore.write('*\n!.gitignore')
        print(f".gitignore file created in {directory}")

    with open(file_path, 'r') as file:
        lines = file.readlines()

    user_data = {}
    format_detected = None
    user_count = 0  # Initialize user counter

    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip().lower().replace(" ", "_")
            value = value.strip()

            if key == "login":
                if user_data:
                    user_count += 1  # Increment counter as we start a new user block
                    save_user_data(user_data, directory, user_count)
                user_data = {}
                format_detected = 'line_by_line'
            if format_detected == 'line_by_line':
                user_data[key] = value

    if user_data and format_detected == 'line_by_line':
        user_count += 1  # Increment for the last user
        save_user_data(user_data, directory, user_count)

def save_user_data(user_data, directory, user_count):
    username = user_data.get('login')
    file_name = f'{directory}/{user_count}_{username}_cookie.json'
    expiration_timestamp = int((datetime.now() + timedelta(days=1000)).timestamp())  # 3 year expiration

    cookies = [
        {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "auth_token", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": user_data.get('auth_token')},
        {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "ct0", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": user_data.get('ct0')},
        {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "login", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": user_data.get('login')},
        {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "password", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": user_data.get('password')},
        {"domain": ".twitter.com", "expirationDate": expiration_timestamp, "hostOnly": False, "httpOnly": False, "name": "mail", "path": "/", "sameSite": "unspecified", "secure": True, "session": False, "storeId": "0", "value": user_data.get('mail')}
    ]

    with open(file_name, 'w') as json_file:
        json.dump(cookies, json_file, indent=2)
    print(f"JSON file {file_name} has been created.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python orderconverter.py <path_to_text_file>")
        sys.exit(1)

    file_path = sys.argv[1]  # Get the file path from command-line arguments
    process_data(file_path)
