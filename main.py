# Importing the clear function from the turtle module and the logo variable from the art module.
from turtle import clear
from art import logo

# Printing the logo variable from the art module.
print(logo)

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    
    highest_bid = 0 
    for bidder in bidding_record:
        bid_amount = (bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")    
            
# This is a while loop. It will keep running until the variable bidding_finished is True.

while(not bidding_finished):
    
   # Asking the user for their name and their bid.
    name = input("What is your name? ")
    price = input("What is your Bid? $")
    
   # Adding the name and price to the dictionary bids.
    bids[name] = price
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    
   # This is an if statement. It checks if the variable should_continue is equal to the string "no".
   # If it is, it sets the variable bidding_finished to True.
   
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
        
   # Checking if the variable should_continue is equal to the string "yes". If it is, it clears the
   # screen.
   
    elif should_continue == "yes":
        print('Aha! OKAY')    
        clear()    
