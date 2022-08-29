# my first case study

products = {'Apricot': 300, 
            'Dates': 400,
            'Almonds': 500,
            'Combo-1':630,
            'Combo-2':810,
            'Combo-3': 720,
            'GiftBox':900
            }


print('''
- - - -- - - - - - - - - - - - - - - - - - - -  - - - - - - - -  - - - - - -  -  - - - - -  - - - - 
AdapatMaple Retail
136, Garia Station Road,
Achimota : 643735
- - - - -  - - - - - - - - - -  -- -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
''')

print('Product(s)\t\tPrice\t(per pack)')
for product in products:
    print(f"{product}\t\t\t : {products[product]}")

print('''
***************************************************************************************************
For free delivery, contact 0244120458
***************************************************************************************************
''')