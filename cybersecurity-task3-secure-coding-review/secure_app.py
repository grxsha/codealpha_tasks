import sqlite3

username = input("Username: ")
password = input("Password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Login")

conn.close()
