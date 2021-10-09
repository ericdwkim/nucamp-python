class QueueIterator:  # TODO
    def __init__(self, items):
        pass

    def __next__(self):
        pass


class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.items is None:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

    def my_items(self):
        return self.items

    def __iter__(self):  # TODO
        return QueueIterator(self)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def valid_flavor(self, flavor):
        return flavor in self.flavors

    def order_formatter(self, order, order_number=-1):
        if order_number == -1:
            return f'Customer: {order["customer"]} -- Flavor: {order["flavor"]} -- Scoops: {order["scoops"]}.'
        return f'{order_number}. Customer: {order["customer"]} -- Flavor: {order["flavor"]} -- Scoops: {order["scoops"]}.'

    def take_order(self, customer: str, flavor: str, scoops: int):
        if not self.valid_flavor(flavor):
            print("Sorry, we don't have that flavor.")
        elif scoops < 1 or scoops > 3:
            print("Choose between 1 and 3 scoops.")
        else:
            print(
                f"Order: {scoops} scoops of {flavor} for {customer} created!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")
        print("\n".join(self.order_formatter(o, i)
              for i, o in enumerate(self.orders.my_items(), 1)))  # <-- bad, do not access Queue()'s items member, see #TODO

    def next_order(self):
        print("\nNext Order Up!")
        print(self.order_formatter(self.orders.dequeue()))


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
