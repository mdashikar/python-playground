# define variable
#message='Hello mars'

# Print Welcome Message
#print(message)

# tuple
# programing_languages = "Python", "Java", "C++", "C#"

# print(type(programing_languages))

#loop

#for lang in programing_languages:
    # print(lang)

#tic-tac-toe game
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player=0, row=0, col=0, just_display=False):
    print("     a  b  c")
    if not just_display:
        game[row][col]= player
    for index, row in enumerate(game):
        print(index, row)

game_board(just_display=True)
game_board(current_player = 1, row_choice = 2, col_choice=0)