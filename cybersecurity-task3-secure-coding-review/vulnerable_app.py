import sqlite3

username = input("Username: ")
password = input("Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Vulnerable to SQL Injection
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Login")

conn.close()
