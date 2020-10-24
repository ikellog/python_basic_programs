def start_intro_h():
    print('---------------------------------------')
    print('Tic Tac Toe, human player mode!')
    print('Game Rules: Enter a number to mark your spot, connect 3 in a row to win!')
    print('Start Game:')
    print('''
    \t\t7 | 8 | 9
    \t\t4 | 5 | 6
    \t\t1 | 2 | 3 ''')

def display_updated_gird(p1_spots, p2_spots):
    '''
    p1_spots is a list of spots taken by X
    p2_spots is a list of spots taken by O
    '''
    spot_dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9'}
    int_to_ltr_convert_dict = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g' ,'8':'h','9':'i'}

    p1_spots_ltr = []
    for i in p1_spots:
        p1_spots_ltr.append(int_to_ltr_convert_dict.get(str(i)))

    for l in p1_spots_ltr:
        spot_dict[l] = 'X'

    p2_spots_ltr = []
    for i in p2_spots:
        p2_spots_ltr.append(int_to_ltr_convert_dict.get(str(i)))

    for l in p2_spots_ltr:
        spot_dict[l] = 'O'
    
    a = spot_dict['a']
    b = spot_dict['b']
    c = spot_dict['c']
    d = spot_dict['d']
    e = spot_dict['e']
    f = spot_dict['f']
    g = spot_dict['g']
    h = spot_dict['h']
    i = spot_dict['i']

    print(f'''
    \t\t{g} | {h} | {i}
    \t\t{d} | {e} | {f}
    \t\t{a} | {b} | {c}''')

def game_body_h():
    open_spots = [1,2,3,4,5,6,7,8,9]
    p1_spots = []
    p2_spots = []
    
    round_num = 5
    while round_num > 0:
        p1_loop = 0
        while p1_loop == 0:
            print('\nPlayable spots are:',open_spots)
            p1_input = input('[X] - Player 1 turn, enter a number: ')
            try:
                if int(p1_input) in open_spots:
                    p1_spots.append(int(p1_input))
                    open_spots.remove(int(p1_input))
                    display_updated_gird(p1_spots,p2_spots)
                    if len(open_spots) == 0:
                        print('end game') # end game function
                        break
                    p1_loop = 1
                else:
                    print('Error, you must enter a number in', open_spots)
            except:
                print('Error, you must enter a number in', open_spots)

        p2_loop = 0
        while p2_loop == 0:
            print('\nPlayable spots are:',open_spots)
            p2_input = input('[O] - Player 2 turn, enter a number: ')
            try:
                if int(p2_input) in open_spots:
                    p2_spots.append(int(p2_input))
                    open_spots.remove(int(p2_input))
                    display_updated_gird(p1_spots, p2_spots)
                    p2_loop = 1
                else:
                    print('Error, you must enter a number in', open_spots)
            except:
                print('Error, you must enter a number in', open_spots)

        round_num -= 1

def win_condition(p1_spots):
    '''
    compares spots taken by X with win combinations, player is winner if matched
    '''
    win_combo = [[1,2,3], [4,5,6], [7,8,9], [1,4,5], [2,5,8], [3,6,9], [1,5,9]]
    
    c = 0 
    while c < 6:
        s = []
        for i in win_combo[0+c]:
            for e in p1_spots:
                if i == e:
                    s.append(e)

        for combo in win_combo:
            if s == combo:
                print('you win')
                break
            else:
                c += 1


# start_intro_h()
# game_body_h()

win_condition([1,7,3,2])