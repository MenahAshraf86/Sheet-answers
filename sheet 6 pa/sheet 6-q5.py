# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 23:06:59 2025

@author: menah
"""

import json

users = [
    {"username": "Menna", "password": "1234"},
    {"username": "Mohammed", "password": "4567"},
    {"username": "Arwa", "password": "789"},
    {"username": "Ashraf", "password": "101112"}
]
file = open('users.json', 'w')
json.dump(users, file)
file.close()
file = open('users.json', 'r')
users = json.load(file)
file.close()
print(f"1st user: {users[0]['username']} >> pass: {users[0]['password']}")
users.append({"username": "Ahmed", "password": "556677$"})
file = open('users.json', 'w')
json.dump(users, file)
file.close()
print("User added successfully")
x = input("Username: ")
y = input("Password: ")
file = open('users.json', 'r')
users = json.load(file)
file.close()
check = False
for user in users:
    if user['username'] == x and user['password'] == y:
        check = True
        break

print("Success!" if check else " Error")