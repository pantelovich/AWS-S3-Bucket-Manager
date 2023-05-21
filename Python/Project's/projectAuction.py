import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders= {}

def findHighestBidder(topBidder):
    highestBid = 0
    winner = ""
    for bidder in topBidder:
        bidAmount = topBidder[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print("The winner is {} with the highest bid of ${}".format(winner.capitalize(), highestBid))


bidding = False
while bidding == False:
    name = input("Please enter your name: ").isalpha()
    bid = int(input("Please enter your bid: $"))
    choice = input("Is there an other person who wants to bid? (yes/no): ").lower()
    bidders[name] = bid
    if choice == "no":
        bidding = True
        findHighestBidder(bidders)
    elif choice == "yes":
        clear_screen()
        bidding = False
