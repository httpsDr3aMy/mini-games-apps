import os, random

def display_board(board):
    print(f'''
    Indeksy planszy:         Obecna plansza:
    -------------           -------------
    | 1 | 2 | 3 |           | {board[0]} | {board[1]} | {board[2]} |
    -------------           -------------
    | 4 | 5 | 6 |           | {board[3]} | {board[4]} | {board[5]} |
    -------------           -------------
    | 7 | 8 | 9 |           | {board[6]} | {board[7]} | {board[8]} |
    -------------           -------------\n''')

def o_move(board, counter):
    o_move = int(input('Gracz O, wybierz numer pola: '))
    if board[o_move - 1] in ['O', 'X']:
        print(f'Pole o indeksie {o_move} jest już zajęte!')
    else:
        board[o_move - 1] = 'O'
        counter += 1
    return counter

def o_move_ai(board, counter):
    random_index = random.randint(1, 9)
    while board[random_index - 1] in ['O', 'X']:
        random_index = random.randint(1, 9)
    board[random_index - 1] = 'O'
    counter += 1
    return counter

def x_move(board, counter):
    x_move = int(input('Gracz X, wybierz numer pola: '))
    if board[x_move - 1] in ['X', 'O']:
        print(f'Pole o indeksie {x_move} jest już zajęte!')
    else:
        board[x_move - 1] = 'X'
        counter += 1
    return counter

def check_win(board):
    for player in ['X', 'O']:
        for i in range(0, 9, 3):
            if board[i] == player and board[i+1] == player and board[i+2] == player:
                print(f'Wygrał {player}')
                return True
        for i in range(3):
            if board[i] == player and board[i+3] == player and board[i+6] == player:
                print(f'Wygrał {player}')
                return True
        if board[0] == player and board[4] == player and board[8] == player:
            print(f'Wygrał {player}')
            return True
        if board[2] == player and board[4] == player and board[6] == player:
            print(f'Wygrał {player}')
            return True
    return False

while True:
    counter = 0
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print('''Witaj w grze "Kółko i krzyżyk"!
Wybierz tryb gry:
1. Gracz vs Gracz
2. Gracz vs Komputer''')
    option = int(input('Wybierz opcję: '))
    match option:
        case 1:
            while counter < 10:
                os.system('cls')
                display_board(board)
                x_move(board, counter)
                if check_win(board) == True:
                    display_board(board)
                    break
                if counter == 9:
                    break
                os.system('cls')
                display_board(board)
                o_move(board, counter)
                os.system('cls')
                if check_win(board) == True:
                    display_board(board)
                    break
                if counter == 9:
                    display_board(board)
                    break
        case 2:
            while counter < 10:
                display_board(board)
                x_move(board, counter)
                if check_win(board) == True:
                    break
                if counter == 9:
                    break
                o_move_ai(board, counter)    
                if check_win(board) == True:
                    display_board(board)
                    break
                if counter == 9:
                    display_board(board)
                    break
