import sys

chances_counter = 0
word = 'slowo'
hidden_word = word

chances = int(input('Ile chcesz mieć sznas: '))
while chances < len(word):
    print('Mniej sznas, niz liter w slowie')
    chances = int(input('Ile chcesz mieć sznas: '))

for i in word:
    hidden_word = hidden_word.replace(i, '_')

while True:
    if hidden_word == word:
        print(f'Zgadles haslo w {chances_counter}. próbach')
        sys.exit()
    user_answer = str(input('Podaj litere: '))
    updated_hidden_word = ''
    for check_letter in hidden_word:
        if check_letter == user_answer:
            print('Podales juz taka litere')
            break
    chances_counter += 1
    for counter, letter in enumerate(word):
        if user_answer == letter:
            updated_hidden_word += letter
        else:
            updated_hidden_word += hidden_word[counter]
            
    if chances <= chances_counter:
        print('Brak możliwych prób!')
        break
    hidden_word = updated_hidden_word
    print(hidden_word)
