def trade(current_player):
    possible_trades = list(current_player.get_possible_trades())
    if len(possible_trades) == 0:
        print("You can't trade")
        return False
    while True:
        print("Choose a trade: ")
        for i in range(len(possible_trades)):
            print("%d:" % i)
            for res, amount in possible_trades[i].items():
                print("    %s: %d" % (res, amount))
        trade_choice = int(input("->  "))
        if trade_choice > 3:
            print("Invalid")
            continue
        trade = possible_trades[trade_choice]
        current_player.add_resources(trade)
        break
