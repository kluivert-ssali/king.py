"""
    Making a database system to store files that are sort of like
    secret files on the computer and are password protected so that you only 
    need to remember that password to see that data again
"""

import sqlite3
import random
​
password = '123456'
username = input("Username(PC):")
​
def id_gen():
    id = ''
    for i in range(10):
        id += str(random.randint(0,10))
    return id
if input("Master Password:") == password:
    safe = sqlite3.connect(f"C:\\Users\\{username}\\Documents\\safe.db")
    cObj = safe.cursor()
    cObj.execute("CREATE TABLE IF NOT EXISTS secrets(ID INT PRIMARY KEY, FILENAME TEXT, TYPE TEXT, FILE BLOB)")
    print("Safe opened")
    while True:
        user_choice = input("***************\nq = quit program\ns = save file\no = open  file\n***************\n:")
        if user_choice == 's':
            user_choice = input("File path:")
            with open(user_choice,'rb') as f:
                blob_data = f.read()
                cObj.execute("INSERT INTO secrets(ID, FILENAME, TYPE, FILE) values(?,?,?,?)",
                    (int(id_gen()),
                    user_choice.split("\\")[-1].split('.')[0],
                    user_choice.split("\\")[-1].split('.')[-1],
                    blob_data))
                safe.commit()
            print("File stored ")
        if user_choice == 'o':
            file_name = input("File name:")
            file_extension = input("File extension:")
            cObj.execute("SELECT FILE FROM secrets WHERE FILENAME = ? AND TYPE = ?",(file_name,file_extension))
            data = cObj.fetchall()
            with open(f"C:\\Users\\{username}\\Desktop\\{file_name}.{file_extension}",'wb') as file:
                file.write(data[0][0])
            print("File opened")
        if user_choice == 'q':
            break   
    cObj.close()
    safe.close()