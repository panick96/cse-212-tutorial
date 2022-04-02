# Queues

Have you ever waited in line at a grocery store, lined up in front of a concert menu, or been on hold with customer service over the phone? Then you have experienced a queue! Queues allow us to store data on a first in first out (FIFO) basis.
***
## Basic Structure
Like previously said, queues use a first in first out basis. It is essentially a list of items where order does matter. Let's say that three people, Bob, Joe, and Sue, drive up to a McDonald's in that order.
### **[Bob, Joe, Sue]**
### 1st, 2nd, 3rd 
 Since Bob was first to the queue he gets his food out first leaving Joe and Sue in the queue. <br>
### **[Joe, Sue]**
### 1st, 2nd 

<br>While Joe is waiting for his food, Sue cannot get her food even if it is ready because queues are FIFO. So Sue has to wait for Joe to get his food before she can get hers. This is the basic idea of a queue.<br>

A queue can hold anything regardless of class. So you can have a queue of numbers, strings, or even other queues. You can also have a queue of different classes such as numbers and strings `[1, "string", {42,43,44}]` but that is seen as bad practice. You should keep the same data type accross the queue. 
***
## Queue.put()
Python has a queues library that we can work with. We will be going over the most important functions that come with that starting with: put().<br> The put() function is used anytime that we want to add something to the queue. 
```python
import queue
my_queue = queue.Queue()

my_queue.put("Bob")
my_queue.put("Joe")
my_queue.put("Sue")
```
Notice the order that we put the items into the queue. What do you think the order of the queue will be?
 
<details><summary>Click here for answer</summary>

The correct order of names is:<br>
1.Bob<br>2.Joe<br>3.Sue<br>

`print(my_queue.queue)`
will return: `deque(['Bob', 'Joe', 'Sue'])`

</details>

***

## Queue.get()
When we want to get the next item in the queue we need to use the `.get()` function. This will remove the next item from the queue and return it. If you have worked with python lists, is similar to the `.pop()` function.
Using our queue from above, what will be printed when we run the following code:<br>
```python
print(my_queue.get())
print(my_queue.queue)
```
<details><summary>Click here for answer</summary>

The first print statement will return: 
`Bob`<br>

The second print statement will return: `deque(['Joe', 'Sue'])`
</details>

### Note:
If you try to use the `.get()` function on an empty queue, you will encounter an error with the python library that was imported. 

***

## Queue.empty()

To ensure that we never get the error mentioned above we can use the `.empty()` function. This function will return a boolean. `True` if there is nothing in the queue or `False` if there is **at least one** item in the queue. So we can use the following code to ensure that we never run into an error by calling `.get()` on an empty queue: 
```python
while not my_queue.empty():
    item = my_queue.get()
    #do stuff
```
What will the output of the following code be?
```python
q = queue.Queue()
print(q.empty())
q.put("Bob")
print(q.empty())
```

<details><summary>Click to see answer</summary>

The first print statement will return `True`<br>
The second print statement will return `False`

</details>

***

## Queue.qsize()
The function `.qsize()` will return an `int` with the number of items in the queue. This is useful for when you want to see how many items you have to deal with before the queue is empty
```python
q = queue.Queue()
q.put("Bob")
q.put("Joe")
q.put("Sue")
print(q.qsize()) # This will print "3"

```
What will be the output for the following code? :
```python
q = queue.Queue()

q.put("Tiger")
q.put("Elephant")
print(q.qsize())

q.get()
q.get()
print(q.qsize())

q.put("Bear")
print(q.qsize())
```
<details><summary>Click to see answer</summary>

The first print statement will return `2`<br>
The second print statement will return `0`<br>
The third print statement will return `1`<br>

</details>

***

## Drive-Thru Problem
A drive thru is a good practical example of a queue. Lets try to implement one. We will have a queue of dictionaries. The first key will be the customers name and the second key will be the meal number they ordered. The item to be put in the queue will look something like this:
```
{"customer_name" : "name",
"meal_number" : int}
```
We will add the items to the queue first and then once all of the customers have been added to the queue, we will handle that order. Once all the orders have been handled on the queue, we will print a successful message.
```python
import queue

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

```
<details><summary>Expected output</summary>

Total customers to serve: 3<br>
Preparing order for: Bob<br>
Tacos ready for Bob!<br>
Customers left to serve: 2<br>
Preparing order for: Joe<br>
Burger and fries ready for Joe!<br>
Customers left to serve: 1<br>
Preparing order for: Sue<br>
Salad ready for Sue!<br>
Customers left to serve: 0<br>
All orders finished!<br>

</details>

***

## Customer Service Call Center Problem
Now it's your turn to write some code. Lets say an online store needs to sort customers calling in. The customer will initially be put into a sorting queue. Then once the customers are all put into the queue, they should be assigned a new queue depending on their receiving department. The departments are: **Returns**, **Order Status**, and **Complaints**. We are going to write a program that takes a customer dictionary with the structure `{"customer_name" : "name", "receiving_dept" : "dept"}`. <br>
### Requirements:
1. Program must use 1 initial queue to receive a group of customers and 3 queues that correspond to each department. 
2. After the customers have been put into the initial queue, the program will put the customer in one of 3 queues depending on the department selected. 
3. Must use the following table of customers:<br>

| Initial Position | Customer | Receiving Department |
| -------- | -------- | -------------------- |
| 1 | Joe | Complaints |
| 2 | Bob | Order Status |
| 3 | Sue | Returns |
| 4 | Nick | Order Status |
| 5 | Kay | Returns |

4. The three receiving queues should be returned with the amount of customers in their queue as well as 
### **DO NOT LOOK UNTIL YOU HAVE TRIED FOR YOURSELF**
<details><summary>Sample Solution</summary>

```python
import queue

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
```
</details>
