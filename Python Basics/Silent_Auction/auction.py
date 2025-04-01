""" A programme to allow a silent bid auction"""
import os
from art import LOGO

bids = {}

while True:
    print(LOGO)
    bidder_name = input("Enter your name: ")
    bid_amount = float(input("Enter your bid amount: £"))
    bids[bidder_name] = bid_amount
    continue_bidding = input(
        "Are there further bidders? (y/n): ").lower()
    os.system('cls')
    while continue_bidding not in ("y", "n"):
        print(f"{continue_bidding} is not a valid option")
        continue_bidding = input(
            "Enter 'n' if there are no further bids: ").lower()
        continue
    if continue_bidding == "n":
        max_value = max(bids.values())
        for key, value in bids.items():
            if value == max_value:
                max_key = key
                print(f"The winning bidder was {max_key}."
                      f"\nThe winning bid was £{max_value:.2f}.")
        break
