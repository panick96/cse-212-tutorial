
# set_1 = {"Bob", "Joe", "Sue"}
# set_2 = {"Nick", "Kay", "Sue"}
# set_3 = set_1.difference(set_2)
# set_4 = set_2.difference(set_1)
# print(set_3) # returns {'Joe', 'Bob'}
# print(set_4) # returns {'Nick', 'Kay'}

# set_1 = {"Bob", "Joe", "Sue"}
# set_2 = {"Nick", "Kay", "Sue", "Bob"}
# set_3 = set_1.intersection(set_2)
# print(set_3) # returns {'Sue','Bob'}

# usernames = {"ironman1", "strongestthor", "hulksmash"}
# not_available = True 
# while not_available:
#     print("Please enter your desired username\n")
#     new_user = input()
#     if new_user in usernames:
#         print("ERROR: Username already taken\n")
#     else:
#         usernames.add(new_user)
#         print(f"User: {new_user} added!")
#         not_available = False
# print(f"Users: {usernames}") 
bank_emails = {"tony_stark@gmail.com", "bruce_banner@yahoo.com", "wanda_maxinov@gmail.com", "thor@asgard.net"}

google_emails = {"bruce_wayne@gmail.com", "diana_prince@gmail.com", "tony_stark@gmail.com", "wanda_maxinov@gmail.com"}

users_to_email = google_emails.intersection(bank_emails)

for email in users_to_email:
    print(f"Emailing {email}...")
    #CODE THAT EMAILS vvvvvvvv
    

    #CODE THAT EMAILS ^^^^^^^^
    print(f"{email} succefully notified.")