import time, os

def countingdown():
    users_time = int(input('Podaj ile chcesz odliczac: '))
    while users_time > 0:
        os.system('cls')
        print(users_time)
        time.sleep(1)
        users_time -= 1

countingdown()
