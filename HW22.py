#Name:
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def doubblecost(self):
        self.cost*=2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
bread=Store(6,1.25,0.5)
chicken=Store(12,6.45,4)
tomato=Store(113,5,1)
#3. Print the stock of all three objects and the cost of the second store item.
print(bread.stock)
print(chicken.stock)
print(tomato.stock)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
chicken.doubblecost()
print(chicken.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
tomato.stock=28
print(tomato.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del bread
try:
    print(bread.weight)
except NameError:
    print("item is out of stock")