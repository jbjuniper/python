#Juniper Python Homework - Jonathan Bock 06/04/20

#DICTIONARIES

shopping_cart = {'pair_of_shoes':   ['1','75'],
                 'tie':             ['1','45'],
                 'gloves':          ['1','35'],
                 'hat':             ['1','65'],
                 'pair_of_pants':   ['1','75'],
                 'shoelaces':       ['1','7'],
                 'pair_of_socks':   ['1','9'],
                 'boxer_shorts':    ['1','7']
                 }

print("\n\nDisplay all the keys in the dictionary\n")
print(f'{shopping_cart.keys()}')

print("\nDisplay all the values in the dictionary\n")
for item, lst in shopping_cart.items():print(f'{lst[0]},{lst[1]}')

sale_items = {item: lst for item, lst in shopping_cart.items() if int(lst[1]) <= 10}
print('\nitems which are <= $10\n')
for item,lst in sale_items.items(): print(f'product - {item}  qty - {lst[0]}  price - ${lst[1]}')


