import queue
my_queue = queue.Queue()

my_queue.put("Bob")
my_queue.put("Joe")
my_queue.put("Sue")

#print(my_queue.queue)
while not my_queue.empty():
    print(f"Queue size: {my_queue.qsize()}")
    print(f"{my_queue.get()}")

# print(my_queue.get())
# print(my_queue.queue)
# print(my_queue.get())
# print(my_queue.get())
#print(my_queue.get())
print("EMPTY")
q = queue.Queue()
q.put("Tiger")
q.put("Elephant")
print(q.qsize())
q.get()
q.get()
print(q.qsize())
q.put("Bear")
print(q.qsize())

#initialize queue
drive_thru = queue.Queue()

#create and add orders to queue
drive_thru.put({"customer_name" : "Bob", "meal_number": 2})
drive_thru.put({"customer_name" : "Joe", "meal_number": 1})
drive_thru.put({"customer_name" : "Sue", "meal_number": 3})

#start handling orders
print(f"Total customers to serve: {drive_thru.qsize()}")
while not drive_thru.empty():
    order = drive_thru.get()
    current_customer = order["customer_name"]
    print(f"Preparing order for: {current_customer}")
    if order["meal_number"] == 1:
        print(f"Burger and fries ready for {current_customer}!")
    elif order["meal_number"] == 2:
        print(f"Tacos ready for {current_customer}!")
    elif order["meal_number"] == 3:
        print(f"Salad ready for {current_customer}!")
    else:
        print(f"Sorry {current_customer}, we don't have what you ordered.")
    print(f"Customers left to serve: {drive_thru.qsize()}")
print("All orders finished!")

#initialize queues
sorting_queue = queue.Queue()
complaints_queue = queue.Queue()
order_queue = queue.Queue()
returns_queue = queue.Queue()

print("Incoming calls")

#add calls to queue
#take notice of order
sorting_queue.put({"customer_name" : "Joe", "receiving_dept" : "Complaints"})
sorting_queue.put({"customer_name" : "Bob", "receiving_dept" : "Order Status"})
sorting_queue.put({"customer_name" : "Sue", "receiving_dept" : "Returns"})
sorting_queue.put({"customer_name" : "Nick", "receiving_dept" : "Order Status"})
sorting_queue.put({"customer_name" : "Kay", "receiving_dept" : "Returns"})
print(f"{sorting_queue.qsize()} calls received.")
print("Sorting customers.")

#loop through sorting_queue until empty
while not sorting_queue.empty():
    customer = sorting_queue.get()
    customer_name = customer["customer_name"]
    dept = customer["receiving_dept"]
    if dept.lower() == "complaints":
        print(f"Adding {customer_name} to {dept} queue.")
        complaints_queue.put(customer)
    elif dept.lower() == "order status":
        print(f"Adding {customer_name} to {dept} queue.")
        order_queue.put(customer)
    elif dept.lower() == "returns":
        print(f"Adding {customer_name} to {dept} queue.")
        returns_queue.put(customer)
    else:
        print("error")

#Display queues
print(f"Complaints queue: {complaints_queue.queue}")
print(f"Order Status queue: {order_queue.queue}")
print(f"Returns queue: {returns_queue.queue}")
