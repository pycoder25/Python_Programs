import os
def user_data():
    while True:
        fname = input("First name: ")
        lname = input("Last  name: ")
        age = input("Age: ")
        data = f'{fname},{lname},{age}\n'

        if os.path.exists("data.txt"):
            a = open("data.txt", "a")
            a.write(data)
            a.close()
            print("File updated")
        else:
            b = open("data.txt", "x")
            b.close()
            c = open("data.txt", "w")
            c.write("First_name, Last_name, Age\n")
            c.close()
            d = open("data.txt", "a")
            d.write(data)
            d.close()
            print("File created and updated.")
       
        print("*********************************")


user_data()
    