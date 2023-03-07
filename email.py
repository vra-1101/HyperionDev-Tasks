#An Email Simulation

class Email():
    def __init__(self, email_content, from_address): 
        self.email_content = email_content
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True 

    def mark_as_spam(self):
        self.is_spam = True

    # def __str__(self):
    #     return f"{self.email_content}, {self.from_address}"

email_1 = Email("Hello!", "sender_1@gmail.com") 
email_2 = Email("Hello_Hello!", "sender_2@gmail.com")
email_3 = Email("Hello_Hello_Hello", "sender_3@gmail.com")
inbox = [email_1, email_2, email_3]
spam_list = []
unread_list = []

# takes the content and email address from the received email to make a new Email object.
def add_email():
        email_address = input ("Please enter your email address: ")
        email_text = input("Please enter the text of your email: ")
        new_email = Email(email_text, email_address)
        inbox.append(new_email)


# returns the number of messages in the store
def get_count():
    messages_num = len(inbox)
    return messages_num


# allows the user to input an index and returns the contents of an email in the list
# has_been_read changes to False.
def get_email():
    email_index = int(input("Please enter the position number of the email you would like to see: "))
    email_display = inbox[email_index]
    email_display.mark_as_read()
    return email_display.email_content
    

# should return a list of all the emails that haven’t been read
def get_unread_emails():
    for email in inbox:
        if email.has_been_read == False:
            unread_list.append(email)
    return unread_list

# should return a list of all the emails that have been marked as spam
def get_spam_emails():
    for email in inbox:
        if email.is_spam == True:
            spam_list.append(email)
    return spam_list

# deletes an email in the inbox.
def delete():
    delete_index = int(input("Please enter the position of the email you would like to delete: "))
    inbox.remove(inbox[delete_index]) 

# main body, creating the menu and calling the functions:
user_choice = ""

while user_choice != "quit":
    user_choice = input("""What would you like to do? Enter:
                        read
                        mark spam
                        send
                        delete
                        see all
                        see spam
                        see unread
                        quit?
                        """).lower()
    if user_choice == "read":
        print(get_email())
    elif user_choice == "mark spam":
        spam_index = int(input("Enter the index of the email which you want to mark as spam: "))
        inbox[spam_index].mark_as_spam()
        spam_list.append(inbox[spam_index])
    elif user_choice == "send":
        add_email()
    elif user_choice == "delete":
        delete()
    elif user_choice == "see all":
        print(f"The number of emails in store is {get_count()}")
    elif user_choice == "see spam":
        print(f"Here is the list of spam emails: {get_spam_emails()}")
    elif user_choice == "see unread":
        print(f"Here is the list of unread emails: {get_unread_emails()}")
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
