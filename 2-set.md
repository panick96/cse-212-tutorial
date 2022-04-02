# Sets

****

If you need to group something together with a having no duplicates a set is the data structure that you are looking for. Sets are very similar to lists. They are a group of unique items. 

## Basic Structure
****
Unlike a list, a set can only have one of each item. 

**[Bob, Joe, Joe, Sue]** - Valid list; Invalid set

**{Bob, Joe, Sue}** - Valid list; Valid set

Because sets have only house unique objects, we can use this to check to see if something is already in the set. Sets uses the entry as both the value and the key. So by seeing if we have something in a list it will always be O(1) look up time 
```python
my_set = {"Bob", "Joe", "Sue"}
name = "Joe"

# The look up time will always be O(1) even if the set had 1 million entries. 
if name in my_set:
    print(f"{name} is in the set.")
else:
    print(f"{name} is not in set")
```
****
## Set.add()
****
The function `.add()` will add an entry into the set. If a set already have the value, this function will do nothing.
```python
my_set = {"Bob", "Joe", "Sue"}
my_set.add("Nick") # adds the name Nick to the set
my_set.add("Bob") # does nothing
print(my_set) # prints the set of FOUR names
```
****
## Set.remove() | .discard() | .clear()
****
The `.remove()` function will remove what ever item that is in the set. If you try to remove an item that is not in the set, it will throw a `KeyError` exception. 
```python
my_set = {"Bob", "Joe", "Sue"}
my_set.remove("Bob") # resulting set = {"Joe", "Sue"}
my_set.remove("Bob") # Throws KeyError
```
If you don't want to worry about the error, you can use the `.discard()` function to ignore the `KeyError`.
```python
my_set = {"Bob", "Joe", "Sue"}
my_set.discard("Bob") # resulting set = {"Joe", "Sue"}
my_set.discard("Bob") # Does nothing
```
If you want to completely wipe your set, you can use the `.clear()` function.
```python
my_set = {"Bob", "Joe", "Sue"}
my_set.clear() # resulting set = {}
```
****
## Set.union()
****
If you need to combine two sets together you can use the `.union()` function. The function takes another set as a parameter. This will add both sets togther **but remember,** sets can only have one unique item at once. So if you need to keep count of something do not use the sets. 
```python
set_1 = {"Bob", "Joe", "Sue"}
set_2 = {"Nick", "Kay", "Sue"}
set_3 = set_1.union(set_2)
print(set_3) # returns {'Kay', 'Nick', 'Sue', 'Joe', 'Bob'}
```
****
## Set.intersection() | .difference()
****
The function `.intersection()` will return a set with common values between both sets. The function takes another set as a parameter.  
```python
set_1 = {"Bob", "Joe", "Sue"}
set_2 = {"Nick", "Kay", "Sue", "Bob"}
set_3 = set_1.intersection(set_2)
print(set_3) # returns {'Sue','Bob'}
```
The function `.intersection()` will return a set with uncommon values between both sets. The function takes another set as a parameter and returns the uncommon parameters of the set that you called the function on.
****
```python
set_1 = {"Bob", "Joe", "Sue"}
set_2 = {"Nick", "Kay", "Sue"}
set_3 = set_1.difference(set_2)
set_4 = set_2.difference(set_1)
print(set_3) # returns {'Joe', 'Bob'}
print(set_4) # returns {'Nick', 'Kay'}
```
****
## Unique usernames
****
To show the power of sets we can set up a problem to make sure that when you enter in a username it will be unique. We can do something like this:
```python
usernames = {"ironman1", "strongestthor", "hulksmash"}
not_available = True 
while not_available:
    print("Please enter your desired username\n")
    new_user = input()
    if new_user in usernames:
        print("ERROR: Username already taken\n")
    else:
        usernames.add(new_user)
        print(f"User: {new_user} added!")
        not_available = False
print(f"Users: {usernames}") 
```
This allows us to enter another user into the usernames set. Instead of the username being lost if there is a duplicate there is a check to see if the username is already used. Even if the usernames set is gigantic, this check will only take O(1) time. 
****
## Notifying users of cyber attack
****
This problem is going to be for you to solve. Google just found out that a large bank just hade their database of emails breached. The bank will give you the set of emails and you will have to cross reference that with the set of emails in Googles database so you will know who to email. Please use the following sets of emails for your program.
```python
bank_emails = {"tony_stark@gmail.com", "bruce_banner@yahoo.com", "wanda_maxinov@gmail.com", "thor@asgard.net"}

google_emails = {"bruce_wayne@gmail.com", "diana_prince@gmail.com", "tony_stark@gmail.com", "wanda_maxinov@gmail.com"}
```
<details><summary>Solution</summary>

```python
bank_emails = {"tony_stark@gmail.com", "bruce_banner@yahoo.com", "wanda_maxinov@gmail.com", "thor@asgard.net"}

google_emails = {"bruce_wayne@gmail.com", "diana_prince@gmail.com", "tony_stark@gmail.com", "wanda_maxinov@gmail.com"}

users_to_email = google_emails.intersection(bank_emails)

for email in users_to_email:
    print(f"Emailing {email}...")
    #CODE THAT EMAILS vvvvvvvv
    

    #CODE THAT EMAILS ^^^^^^^^
    print(f"{email} succefully notified.")
```
</details>

