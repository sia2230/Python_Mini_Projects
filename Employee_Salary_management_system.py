import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="#12345",
    database="Employees"
)
my_cursor=db.cursor()
# show all the databases present on system
my_cursor.execute("Show DATABASES")
for i in my_cursor:
    print(i)


# create a database name Employees

# my_cursor.execute("create database Employees")
# db.commit()

#creating table name: Record

# my_cursor.execute("CREATE TABLE Record (Id int primary key,Name varchar(20),Post varchar(30),Salary float)")
# db.commit()

#Adding data to table
# query="Insert into Record(Id,Name,Post,Salary) VALUES (%s,%s,%s,%s)"
# VALUE=[(1,"Ayushi kharpuse","Designer",90000),
#         (2,"Anuska Ingle","Product lead",89000),
#         (3,"Avanti Jaiswal","Backend Developer",90000),
#         (4,"Bhavna Dhage","Tester",86000),
#         (5,"Pravin Choudhary","Backend Developer",90000)]
# my_cursor.executemany(query,VALUE)
# db.commit()
def add_Employee():
    try:
        id_input=int(input("Enter id of Employee :"))
        name_input=input("Enter name of Employee :")
        post_input=input("Enter the post of Employee :")
        salary_input=float(input("Enter salary of Employee :"))
        query="Insert into Record(Id,Name,Post,Salary) VALUES (%s,%s,%s,%s)"
        VALUE=[(id_input,name_input,post_input,salary_input)]
        my_cursor.executemany(query,VALUE)
        db.commit()
        print("Employee added Successfuly ")
    except:
        print("Exception occur")
    finally:
        extra=input(" Do you want to add more employees(y/n) :")
        if extra=='y':
            add_Employee()
        else:
            main()
            
def remove_Employee():
    print("you can remove Employee by there ID number")
    extra=int(input("Enter Id of Employee you want to remove from Company : "))
    try:
        my_cursor.execute(f"DELETE FROM Record WHERE Id ={extra}")
        db.commit()
        print("Employee removed Successfuly ")
    except:
        print("Exception occur")
    finally:
        extra=input(" Do you want to remove more employees(y/n) :")
        if extra=='y':
            remove_Employee()
        else:
            main()    
    
def promote_Employee():
    extra=int(input("enter the id of the employee : "))
    post_name=input("enter the post name employee is promoted : ")

    try:
        my_cursor.execute(f"Update Record SET Post={post_name} where Id={extra}")
        db.commit()
        print(" Successfuly ")
    except:
        print("Exception occur")
    finally:
        extra=input(" Do you want to update data of  more employees(y/n) :")
        if extra=='y':
            promote_Employee()
        else:
            main()        
def Display_all_employee():
    query="SELECT * FROM Record"
    my_cursor.execute(query)
    r = my_cursor.fetchall()
    for i in r:
        print("-"*56)
        print("Employee Id       :        ", i[0])
        print("Employee Name     :        ", i[1])
        print("Employee Post     :        ", i[2])
        print("Employee Salary   :        ", i[3])
        print("-"*56)

    main()
def check_employee():
    extra=int(input("Enter Id of employee you want to check : "))
    try:
        my_cursor.execute(f"SELECT * FROM Record WHERE Id={extra}")
        r = my_cursor.fetchall()
        for i in r:
            print("-"*56)
            print("Employee Id       :        ", i[0])
            print("Employee Name     :        ", i[1])
            print("Employee Post     :        ", i[2])
            print("Employee Salary   :        ", i[3])
            print("-"*56)
   
    except:
        print("Exception occur")
    finally:
        extra=input(" Do you want to check more employees(y/n) :")
        if extra=='y':
            check_employee()
        else:
            main()    
def main():
    print('='*56)
    print("------------  1.SHOW EMPLOYEE OF COMPANY    ------------")
    print("------------  2.ADD EMPLOYEE TO THE COMPANY ------------")
    print("------------  3.REMOVE EMPLOYEE             ------------")
    print("------------  4.PROMOTE                     ------------")
    print("------------  5.CHECK EMPLOYEES             ------------")
    print("------------  6.EXIT                        ------------")
    print('='*56)
    print()
    input2()
def input2():
    input1=int(input("Enter your Choice : "))
    if input1==1:
        Display_all_employee()
    elif input1==2:
        add_Employee()
    elif input1==3:
        remove_Employee()
    elif input1==4:
        promote_Employee()
    elif input1==5:
        check_employee()
    elif input1==6:
        exit
    else:print("Invalid Input ! ! !")


main()   

    
