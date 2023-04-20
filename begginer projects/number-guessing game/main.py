from random import randint
random_number = randint(1, 20)
number_of_tries = int(input('Ile chcesz miec prob? '))
counter = 0
while True:
    user_answer = int(input('Wybierz liczbe z zakresu 1-20: '))

    if number_of_tries == 0:
        print('Brak prób!')
        break    
    elif user_answer > random_number:
        number_of_tries -= 1
        counter += 1
        print(f'Liczba podana od ciebie jest większa. Pozostalo ci {number_of_tries} prób.')
    elif user_answer < random_number:
        number_of_tries -= 1
        counter += 1        
        print(f'Liczba podana od ciebie jest mniejsza. Pozostalo ci {number_of_tries} prób.')
    elif user_answer == random_number:
        counter += 1 
        print(f'Gratulacje zgadles liczbe! Zgadles w {counter}. próbach.')
