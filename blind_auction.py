ans = True
silence_bid = {}
bid_winner_name = ""
bid_winner_prize = 0
while ans:
# TODO-1: Ask the user for input
    user_name = input("What is your name:\n")
    bid_prize = int(input("Place your bid: \n"))
# TODO-2: Save data into dictionary {name: price}
    silence_bid[user_name] = bid_prize
# TODO-3: Whether if new bids need to be added
    need_continue = input("Do you want to contine this bid, write to 'no' for continue").lower()
    if need_continue == "no":
        ans=False
    print("\n"*20)
# TODO-4: Compare bids in dictionary
for name in silence_bid:
    if silence_bid[name] >= bid_winner_prize:
        bid_winner_name = name
        bid_winner_prize = silence_bid[name]
print(f"Winner name is {bid_winner_name} and the bid is {bid_winner_prize}")
