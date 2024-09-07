print("Welcome to the secret auction program");

bidders_record = {}
is_continue = True

def find_winner():
    winner = ""
    higher_bid = 0
    for user in bidders_record:
        if bidders_record[user] > higher_bid:
            winner = user
            higher_bid = bidders_record[user]
    print(f"The winner is {winner} with a bid of ${higher_bid}")

while is_continue:
    valid_name = False
    username = ""
    while not valid_name:
        username = input("What is your name? \n").lower()
        if username in bidders_record:
            print('Name has been used, please try another one')
        else:
            valid_name = True
    user_bid = int(input("What's your bid? \n$"))
    bidders_record[username] = user_bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == 'yes' or should_continue == 'y':
        print("\n" * 20)
    else:
        is_continue = False
        find_winner()
