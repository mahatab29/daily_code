requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")
#when the list is empty if statement returns as false so it sees condition as fail
