# define variable
#message='Hello mars'

# Print Welcome Message
#print(message)

# tuple
# programing_languages = "Python", "Java", "C++", "C#"

# print(type(programing_languages))

#list 
'''friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1, "Kevin")

# friends.remove("Kevin")
print( friends )
print( friends.index("Oscar") )
print( friends.count("Angela") )
friends.sort()
print( friends )'''


#loop

#for lang in programing_languages:
    # print(lang)

#tic-tac-toe game

'''game = [[1, 0, 0],
        [2, 2, 2],
        [2, 1, 2],]
def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        print("     a  b  c")
        if not just_display:
            game_map[row][col]= player
        for index, row in enumerate(game_map):
            print(index, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you enter row/column as 0, 1 or 2?", e)
    except Exception as e:
        print("Something went wrong!!! Try again", e)

game = game_board(game, just_display=True)
game = game_board(game, player=1, row=2, col=0)'''


import itertools
game = [[1, 0, 0],
        [2, 2, 2],
        [2, 1, 2],]


def win_check(current_game):
    #Horizontal 
    for row in enumerate(current_game):
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'Player {row[0]} is the winner horizontally!')
        
    #Diagonal
    diags = []
    for col,row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print(f'Player {diags[0]} is the winner Diagonally (/)!')
        

    diags = []
    for ix in range(len(current_game)):
        diags.append(current_game[ix][ix])
        if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print(f'Player {diags[0]} is the winner Diagonally (\\)!')
       

    #Vertical     
    for col in range(len(current_game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f'Player {check[0]} is the winner horizontally!')

def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        print("     a  b  c")
        if not just_display:
            game_map[row][col]= player
        for index, row in enumerate(game_map):
            print(index, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you enter row/column as 0, 1 or 2?", e)
    except Exception as e:
        print("Something went wrong!!! Try again", e)

#game = game_board(game, just_display=True)
#game = game_board(game, player=1, row=2, col=0)

play = True
while play:
    game = [[1, 0, 0],
            [2, 2, 2],
            [2, 1, 2],]
    
    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: #{current_player}")
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player , row_choice, column_choice)


#win_check(game)