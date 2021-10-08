class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    # customer, flavor = strings; scoops = integer
    def take_order(self, customer, flavor, scoops):

        # declare local attributes
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops

        # check if flavor is in list of flavors
        # check if # of scoops is b/w 1 -3 (inclusive) scoops
        if (flavor in self.flavors) and (scoops in range(1, 4)):
            # print success message
            print("order has been created")

        # print error message if conditionals not met for order
        else:
            print("flavor not in list or # of scoops must be b/w 1 -3")

        order = {"customer": customer, "flavor": flavor, "scoops": scoops}

# def show_all_orders():
#     # do stuff

# def next_order():
#     # do stuff
