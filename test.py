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

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #Horizontal 
    for row in game:
        print(row)
        if all_same(row):
            print(f'Player {row[0]} is the winner horizontally!')
            return True
        
    #Diagonal
    diags = []
    for col,row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner Diagonally (/)!')
        return True
       

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f'Player {diags[0]} is the winner Diagonally (\\)!')
        return True
        

    #Vertical     
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f'Player {check[0]} is the winner horizontally!')
            return True
    return False    
def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        if game_map[row][col] != 0:
            print("This position is occupado! Choose another position")
            return game_map, False
        print("   0  1  2")
        if not just_display:
            game_map[row][col] = player
        for index, row in enumerate(game_map):
            print(index, row)
        return game_map, True
    except IndexError as e:
        print("Error: make sure you enter row/column as 0, 1 or 2?", e)
        return game_map, False
    except Exception as e:
        print("Something went wrong!!! Try again", e)
        return game_map, False

#game = game_board(game, just_display=True)
#game = game_board(game, player=1, row=2, col=0)

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],]
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: #{current_player}")
        played = False
        while not played:
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        if win_check(game):
            game_won = True    
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == 'y':
                print("Restarting")
            elif again.lower() == "n":
                print("Bye, see you next time!!!")
                play = False
            else:
                print("Not a valid answer!!!")
                play = False



#win_check(game)