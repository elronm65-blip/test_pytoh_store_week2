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



  
def add_item_for_order(products:list , order:dict ):
    print(products)
    print("chosse items and quantity ,if you wwant stopp choose 0 for id and quantity")
    order["id"] += 1
    while True:
        item_id = int(input("choose id of item"))
        quantity = int(input("choose quantity"))
        if item_id == 0 and quantity == 0:
            return order
        item = {"product_id":item_id, "quantity":quantity}
        order["items"].append(item)
        
        
        
    
def total_price_order(order,products):
    total_after_dis = 0
    total = 0
    all_items = order["items"]
    for item in all_items:
        for product in products:
            if product["id"] == item["product_id"]:
                sum  = product["price"] * item["quantity"]
                total += sum
    if total < 300:
        total_after_dis = total            
    if total >= 300 and total < 700:
        total_after_dis = total *(1- (5/100))
    if total >= 700 and total < 1500:
             total_after_dis = total *(1- (10/100))
    if total >= 1500:
         total_after_dis = total *(1- (15/100))
    order["total"] = total
    order["total_after_dis"] =total_after_dis 


    if order["id"] == 1:
        with open("orders.json", "w", encoding="utf-8") as file:
                 json.dump(order, file,indent=2, ensure_ascii=False)
          
    else:
        with open("orders.json", "r", encoding="utf-8") as file:
            loaded = [json.load(file)]  
            loaded.append(order) 
        with open("orders.json", "w", encoding="utf-8") as file:
            json.dump(loaded, file,indent=2, ensure_ascii=False)
          
    return f'total:{total} after dis:{total_after_dis} and update to ordders list'     
            


   