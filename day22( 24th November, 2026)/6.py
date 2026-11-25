def full_name(f,l):
    name= f"{f} {l}"
    return name.title()


while True:
    print(f"Enter 'q' to exit")

    first = input("enter your first name: ")
    if first == 'q':
        break
    last = input("enter your last name: ")
    if last == 'q':
        break
    formated = full_name(first, last)
    print(f"\nHello, {formated}")
