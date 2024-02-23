# def greet(name):
# message = f"hello {name}"
# new_message = message.title()
# print("Hey hey")
# return new_message


#def greet():
#    message = "hello"
#    new_message = message.title()
#    print("Hey hey")
#    return new_message


# greeting = greet(input("What is your name? "))
#greeting = greet()
# print(greeting)

def greet(message):
    new_message = message.capitalize()
    print("HEY HEY")
    return new_message


user_entry = input("Which greeting do you like? ")
greeting = greet(user_entry)
print(greeting)
