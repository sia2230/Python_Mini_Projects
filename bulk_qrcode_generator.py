import datetime
import mysql.connector
import qrcode
import os

# Set the path for the directory
path = "D:\Techwalnut\Task"#folder path you want to generate the folder for bulk og qrcodes
name_folder = input("Enter folder name for saving QR codes (or press Enter for 'Default by custom name'): ").strip() or f"{custom_name}"
path = os.path.join(path, name_folder)

# Check if the directory exists before creating it
if not os.path.exists(path):
    os.mkdir(path)
else:
    print(f"The directory '{path}' already exists.")
    exit()

url=input("enter the url :")
initial_value=int(input("enter initial value from which you want qrcode number : "))
final_value=int(input("enter the value you want qrcode upto : "))

def qr_generator(url, initial_range, final_range):
    for i in range(initial_range, final_range + 1):
        data = url
        print(data)
        img = qrcode.make(data)
        img.save(os.path.join(path, f"qrcode_{i}.png"))
    # print("----------DONE-----------")
    
    print("----------DONE-----------")

qr_generator(url,initial_value,final_value)
