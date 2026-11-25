def get_formetted_name(first_name, last_name):
    name = f"{first_name} {last_name}"
    return name.title()
#infinit loop
while True:
    f_name= input("Enter your first name: ")
    l_name= input("Enter your last name: ")
    x= get_formetted_name(f_name, l_name)
    print(f"Your full name would be: {x}")
