import sqlite3
import datetime

connection = sqlite3.connect('analiza_wydatkow/analizawydatkow.db') #there type your database directory
cur = connection.cursor()

def make_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS expense(expense_name text, expense_cost real, expense_month integer)""")

def getting_expense(connection):
    while True:
        try:
            expense_name = input('Nazwa wydatku: ')
            expense_cost = float(input('Ile kosztował ten wydatek: '))
            expense_month = int(input('Podaj indeks miesiąca, w którym dokonano wydatku: '))
            cur.execute("""INSERT INTO expense(expense_name, expense_cost, expense_month) VALUES(?, ?, ?)""",(expense_name, expense_cost, expense_month,))
            connection.commit()
            break
        except ValueError:
            print('Błędna odpowiedź')

def current_month_expense(connection):
    current_time = datetime.datetime.now()
    month = current_time.month
    cur.execute("""SELECT * FROM expense WHERE expense_month = ?""", (month,))
    result = cur.fetchall()
    print(f'Obecny miesiąc: {month}')
    for row in result:
        print(f'Nazwa wydatku: {row[0]}, Ile kosztował wydatek: {row[1]}')

def statistics(connection):
    cur.execute("""SELECT expense_cost FROM expense""")
    result = cur.fetchall()
    list_total_amount_this_month = [row[0] for row in result]

    cur.execute("""SELECT expense_cost FROM expense WHERE expense_month = ?""",(datetime.datetime.now().month,))
    result = cur.fetchall()
    average_expense_this_month = sum(row[0] for row in result) / len(result)

    average_expense_all = sum(list_total_amount_this_month) / len(list_total_amount_this_month)

    print("Średni wydatek w tym miesiącu [zł]:", average_expense_this_month)
    print("Wszystkie wydatki [zł]:", sum(list_total_amount_this_month))
    print("Średni wydatek [zł]:", average_expense_all)

while True:
    make_db()
    print('1. Dodaj wydatek.')
    print('2. Wyświetl wydatki w tym miesiącu.')
    print('3. Statystyki.')
    print('4. Wyjdź.')

    user_answer = input('Wybierz opcję: ')

    if user_answer == '1':
        getting_expense(connection)

    elif user_answer == '2':
        current_month_expense(connection)

    elif user_answer == '3':
        statistics(connection)
    elif user_answer == '4':
        connection.close()
        break