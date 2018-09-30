TICKET_PRICE = 10
SERVICE_CHARGE = 2  

tickets_remaining = 100  

def calculate_price(ticketNumber):
    return (TICKET_PRICE * ticketNumber) + SERVICE_CHARGE


while tickets_remaining >=1:
    

    print("There are {} tickets available now".format(tickets_remaining))
    name = input("What is your name? ")
    tickets_number = input("Hello {}! How many tickets would you like? ".format(name))
    
    try:
        tickets_number = int(tickets_number)
        if tickets_number > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
                             
    except ValueError as err:
        print("Oh no we ran into an issue, {} please try again!".format(err))  
    else:
        ammount_price = calculate_price(tickets_number)
        print("Total price of the tickets is: ${} ".format(ammount_price))
        confirmed = input("Would you like to confirm your purchase? (Y/N) ")
        if confirmed.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("Thank you of your purchase. {} pieces of tickets SOLD for you".format(tickets_number))
            tickets_remaining -= tickets_number
        
        else:
            print("Thank you anyways, {} ".format(name))

print("Sorry, all tickets SOLD OUT")

    