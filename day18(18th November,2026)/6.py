Command = "yes"
while Command in ['yes','again']  :
    height = int(input("How tall are you, in inches? "))
    if height >= 48 :
        print(f"\nYou're tall enough to ride!")
    else:
        print("\nYou'll be able to ride when you're a little older.")
    Command = input("Wanna start the programme?(yes/no) ").lower()


