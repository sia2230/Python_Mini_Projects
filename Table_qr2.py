import os#needed here to traverse directory/folder
import cv2#for scanner
import csv#for making csv file
import re #import for spliting list by number 

#path of folder
def read_qr_code(filename):
    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        print("exception")
        return
headers=["Name", "Encoded","status"]
table_data=[]


def make_table(path):
    for filename in os.listdir(folder_path):#folder traversing(traverse all files from folder)
        status=""#for checking if compressed url of all qrcode generated in a folder is same or not
        read=read_qr_code(f"{path}/{filename}")#scan every file from folder and return the scanned output 
        print(read)
        #list2=re.split('\d+',read)
        #print(list2)
        list2=re.split(f'({re.escape(delimiter)})', read)
        list2_modified=[list2[0]+list2[1],list2[2]]#it will create a list which contain domain+custom_name and extract the number of file generated
        #print(list2_modified)#for testing only

        if list1_modified[0]==list2_modified[0]:#list1[0]==list2[0]:#checking if compressed url is same or not
            status="pass"
            
        else:
            status="fail"
        table_data.append([filename,read,status])#append for every file present in folder
    #for csv file (like data insertion )  
    with open("qr_data.csv","w")as t_data:
        table_data1=csv.writer(t_data)
        table_data1.writerow(headers)
        table_data1.writerows(table_data)

folder_path="D:/Techwalnut/Task/folder"#path of folder we want to traverse
read1=read_qr_code("D:/Techwalnut/Task/folder/qrcode1.png")#qrcode file from that folder


#list1=re.split('\d+',read1)#extract number from file name it will help to compare url of all qrcode in same folder is same or not
#above list1 logic to get the domain/custom_name when custom_name contain any number
# print(read1)

#delimiter = "qrcode"#giving custom name explicitly or we can take input from user 
delimiter=input("enter the custom name of url : ")
list1=re.split(f'({re.escape(delimiter)})', read1)
list1_modified=[list1[0]+list1[1],list1[2]]
print("outside",list1_modified)#just for checking
make_table(folder_path)#calling make_table function which contain mechanism of making table as we need


