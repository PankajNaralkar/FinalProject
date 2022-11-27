import json
class Restaurent:
    def __init__(self):
        self.register={}
        self.register_id=len(self.register)+1
        
    def add_register_user(self):
        self.Fullname=input("Enter Registers Fullname: ")
        self.PhoneNo=int(input("Enter Phone Number: "))
        self.Email=input("Enter Email id: ")
        self.Address=input("Enter Address: ")
        self.username=input("Enter Username:")
        self.Password=int(input("Enter Password:  "))
        self.item={"Fullname":self.Fullname,"PhoneNo":self.PhoneNo,"Email":self.Email,"address":self.Address,"Password": self.Password}
        self.register_id=len(self.register)+1
        self.register[self.register_id]=self.item
        print(self.item)
        print(self.register)
        with open("Register_data.json","w") as f:
            
            json.dump(self.register,f)
        print("Registration successfully. ")
        
    def User_login(self):
        self.Username = input("Username: ")
        self.Password = input("Password: ")
         
        with open("Register_data.json","w") as f:
            f.read("\n" + self.Fullname + ',' + self.Password )
            for i in f:
                a,b = i.split(',')
                b = b.strip()
                a = a.strip()
                if(a== self.Username and b== self.Password):
                    print("Login successful")
                else:
                    print("Login failed. Wrong Username or Password.")     
                f.close() 
                break
       

         
x=Restaurent()
x.add_register_user()
x.User_login()