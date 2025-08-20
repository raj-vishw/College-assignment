cost = int(input("Enter cost price:"))
selling = int(input("Enter selling price:"))


if ( cost < selling ):
    profit = selling - cost
    print(f"The profit is {profit}.")
elif (cost > selling)  :
    loss = cost - selling
    print(f"The lose is {loss}")
else :
    print("There was not any profit or loss.")
