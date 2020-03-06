##class product:
##    def __init__(self, prdt_name, prdt_id, prdt_type):
##        self.prdt_id=prdt_id
##        self.prdt_name=prdt_name
##        self.prdt_type=prdt_type  
##
##
##
##
##class product_type:
##    def __init__(self, prdt_name, prdt_id):
##        self.prdt= prdt_id
##        self.prdt=prdt_name
        

items = {}

class product:
    def __init__(self, prdt_name, prdt_id, prdt_type):
        self.prdt_id=prdt_id
        self.prdt_name=prdt_name
        self.prdt_type=prdt_type

def add_product(product):
    if not items.get(product.prdt_id):
        items[product.prdt_id] = 1
        
    else:
        items[product.prdt_id] =+ 1
        
product = product('Furniture',200, 'Cata' )


add_product(product)

print(items)


class inventory:
    def __init__(self, prdt_id, quantity):
        
        self.prdt_id=prdt_id
        self.quantity=quantity
        
def add_product(product):
    if not items.get(product.prdt_id):
        items[product.prdt_id] = 1
        
    else:
        items[product.prdt_id] =+ 1
        
product = inventory('Furniture',200, )
#prdt1 = product(101, 'Books' 'Languages')

add_product(product)


print(items)








    
        
        
        

