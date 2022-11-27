import json
print('Enter correct username and password combo to continue')
count=0
while count < 1:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Admin' and username=='Admin':
        print('Access granted')
        class Restaurent:
            def __init__(self):     
                self.foods={}
                self.food_id=len(self.foods)+1      
            def add_food_items(self):
                self.name=input("Enter the Food Item name: ")
                self.Quantity =int(input("Enter Food Quantity : (kg) "))
                self.Price=int(input("Enter Food Price : "))
                self.Disccount=int(input("Enter Disccount : "))
                self.Stock = int(input("Enter Stock Value : "))
                self.item={"name":self.name,"Quantity":self.Quantity,"Price":self.Price,"Disccount":self.Disccount,"Stock":self.Stock}
                self.food_id=len(self.foods)+1
                self.foods[self.food_id] = self.item
                print(self.item)
                print(self.foods)
                with open("food_data.json","w") as f:
                    json.dump(self.foods,f)
                print("Item added Successfully ")

            def view_food_items(self):
                with open('food_data.json') as y:
                    data = json.load(y)
                print("Available Food Items")
                print(data)
        
            def remove_food_items(self):
                x = int(input("Enter the Food id which you want to delete :"))
                del self.foods[x]
                print("Remaining items available",self.foods)       
        x=Restaurent() 
        x.add_food_items()
        x.add_food_items()
        x.view_food_items()
        x.remove_food_items()
        break
    else:
        print('Access denied. Try again.')
        count += 1
        