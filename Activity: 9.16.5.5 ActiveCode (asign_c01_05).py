
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    name, qty, cost = item.split(',')
    print("The store has {} {}, each for {} USD.".format(qty, name, cost))

#
#product = [word[0:3] for word in inventory if word]
#quantity =
#price =


#print(product)

