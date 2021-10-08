from logo import logo
print(logo)
start = input("Do you wish to play a game of tic-tac-toe? (Y/N): ").lower()
if start == "y":
    GRID = {
        "1": ["  ", "|", "  ", "|", "  "],
        "2": ["  ", "|", "  ", "|", "  "],
        "3": ["  ", "|", "  ", "|", "  "],
    }
    HORIZONTAL_LINE = "========"
    X = "X "
    O = "O "
    ROUND_COUNT = 0


    def show_arena():
        for row in GRID:
            print(''.join(GRID[row]))
            if row != '3':
                print(HORIZONTAL_LINE)


    def check_if_done(symbol):
        for key in GRID:
            if GRID[key][0] == GRID[key][2] == GRID[key][4] == symbol:
                return True, symbol
        for i in range(0, 5, 2):
            if GRID["1"][i] == GRID["2"][i] == GRID["3"][i] == symbol:
                return True, symbol
        diagonal_1 = eval("GRID['1'][0] == GRID['2'][2] == GRID['3'][4] == symbol")
        diagonal_2 = eval("GRID['1'][4] == GRID['2'][2] == GRID['3'][0] == symbol")
        if diagonal_1 or diagonal_2:
            return True, symbol
        else:
            return False, symbol


    def check_overwrite(location, symbol, factor, cords):
        global validity_player_1, validity_player_2
        err_overwrite = "Error: Overwriting on an existing symbol"
        if location == "  ":
            GRID[cords[0]][int(cords[1]) + factor] = symbol
            if symbol == X:
                validity_player_1 = False
            else:
                validity_player_2 = False
        else:
            print(err_overwrite)


    def put_symbol(co_ors, symbol):
        co_ors = list(co_ors)
        if int(co_ors[0]) <= 3:
            # print(co_ors)
            if co_ors[1] == '1':
                location = GRID[co_ors[0]][int(co_ors[1]) - 1]
                check_overwrite(location=location, symbol=symbol, factor=-1, cords=co_ors)
            elif co_ors[1] == '2':
                location = GRID[co_ors[0]][int(co_ors[1])]
                check_overwrite(location=location, symbol=symbol, factor=0, cords=co_ors)
            elif co_ors[1] == '3':
                location = GRID[co_ors[0]][int(co_ors[1]) + 1]
                check_overwrite(location=location, symbol=symbol, factor=1, cords=co_ors)
            else:
                print("Invalid column coordinate!")
        else:
            print("Invalid row coordinate!")
    print("Instructions: In order to enter the position where you want to put an X or a O,\n"
          "enter the row and column as a 2 digit number. For example, 12 will be interpreted\n"
          "as the the cell in the 1st row and 2nd column. ")

    while ROUND_COUNT < 9:
        validity_player_1 = True
        validity_player_2 = True
        while validity_player_1:
            player1 = input("Player 1: ")
            put_symbol(co_ors=player1, symbol=X)
            show_arena()
        ROUND_COUNT += 1
        if ROUND_COUNT == 9:
            print("It is a draw!")
            break
        game_on = check_if_done(symbol=X)
        if game_on[0] and game_on[1] == X:
            print('Player 1 wins!')
            break
        while validity_player_2:
            player2 = input("Player 2: ")
            put_symbol(co_ors=player2, symbol=O)
            show_arena()
        ROUND_COUNT += 1
        game_on = check_if_done(symbol=O)
        if game_on[0] and game_on[1] == O:
            print('Player 2 wins!')
            break
