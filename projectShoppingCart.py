class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.__cart = []

    def add_to_cart(self, item):
        self.__cart.append(item)

    def remove_from_cart(self, index):
        del self.__cart[index]

    def calculate_total(self):
        total = 0
        for item in self.__cart:
            total += item.price
        return total

    def display_cart(self):
        print("Your cart:")
        for i, item in enumerate(self.__cart):
            print(f"{i + 1}. {item.name}: ${item.price}")
        print()

store = Store()

print("Hello, welcome to our store!")
while True:
    store.display_cart()
    print(f"Your total is: ${store.calculate_total()}")

    print("Press 1 to add item")
    print("Press 2 to remove item")
    print("Press 3 to quit")
    user_input = input("Please enter a command: ")
    if user_input == "3":
        break
    elif user_input == "1":
        item_name = input("Please give the item a name: ")
        price = float(input("Please provide a price: "))
        store.add_to_cart(Item(item_name, price))
    elif user_input == "2":
        index = int(input("Please enter the index of the item to remove: ")) - 1
        if index >= 0 and index < len(store._Store__cart):
            store.remove_from_cart(index)
        else:
            print("Invalid index!")
    else:
        print("Sorry, command not recognized")
