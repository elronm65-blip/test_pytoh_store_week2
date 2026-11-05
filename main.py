from build_func import add_item_for_order , total_price_order
import json
from pathlib import Path
products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]

order = {
    "id": 0,
    "items":[
              ],
    "total": "",
    "total_after_dis":"",
    "status": "open"
}

orders =[]

while True:


    print("========== ORDER MANAGER ==========",
    "1. Create" ,
    "2. Show all orders",
    "3. Find order by ID",
    "4. Close order",
    "5. Show sales report",
    "0. Exit",
    "Choose option: "
    )
    choise = input("choise option 0 -5")
    
    if choise == "1":
        my_order = add_item_for_order(products, order )
        print(total_price_order(my_order,products ))
        print(my_order)
        # with open("orders.json", "r", encoding="utf-8") as file:
        #     loaded = json.load(file) 
         
             
        
             
    if choise == "2" :
        with open("orders.json", "r", encoding="utf-8") as file:
            read_all = json.load(file)  
        print("oo")
        print(read_all)      
       
    