from replit import clear
from art import logo

print(logo)
print("\n Welcome to simple auction program, please enjoy!")

stored_name_bid = {}
bidding_session = False


#function to find the highest bid
def highest_bid_checker(bidding_record):
  #track the highest amount
  highest_bid_amount = 0

  winner_of_the_bid = ""
  
  for bidding_value in bidding_record:
    bid_amount = bidding_record[bidding_value]
    if bid_amount > highest_bid_amount:
      highest_bid_amount = bid_amount
      winner_of_the_bid = bidding_value
  print(f" The winner is {winner_of_the_bid.title()}, and the amount is ${highest_bid_amount}.")
    

while not bidding_session:
  player_name = input(" What is your name?: ")
  player_bid = int(input(" Please enter the amount of your bid: $"))
  
  #store the name and bid amount
  stored_name_bid[player_name] = player_bid

  other_bidders = input("\n Are there other bidders? [type Y or N]: ").lower()
  if other_bidders == 'n':
    bidding_session = True
    highest_bid_checker(stored_name_bid)
  elif other_bidders == 'y':
    clear()
    
