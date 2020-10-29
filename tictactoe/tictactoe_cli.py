
print('---------------------------------------')
print('Welcome to Ultimate Tic Tac Toe!\n')
print('Enter "c" - play against AI\nEnter "h" - play against human')

play_loop = 0
while play_loop == 0:
    user_input = input('Choose play mode: ')
    try:
        if user_input == 'c':
            print('feature not yet available')
        elif user_input == 'h':
            # start_game_human()
            play_loop = 1
        else:
            print('Error, you must enter "c" [play against AI] or "h" [play against human]')
    except:
        print('Error, you must enter "c" or "h" to start game')
