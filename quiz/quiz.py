import json
points = 0
questions_counter = 0
user_answer = ''
with open('quiz/quiz.json', encoding="utf-8") as file:
    content = json.load(file)
for question in content:
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    user_answer = str(input('Wybierz opcję: '))
    print()
    user_answer = user_answer.lower()
    questions_counter += 1
    if user_answer == question['prawidlowa_odpowiedz']:
        points += 1
        print('Poprawna odpowiedź')
    else:
        print('Zła odpowiedz')
print(f'Oto twoja liczba punktów {points} na {questions_counter}')