import datetime
import winsound

future_alarms = []

def alarm_turning_on(future_alarms):
    future_alarm = input('O której chcesz włączyć alarm: ')
    days_future_alarm = input('W jakie dni chcesz włączyć alarm: ')
    how_many_times_future_alarm = int(input('Ile razy chcesz włączyć alarm: '))
    label_of_alarm = input('Podaj etykiete alarmu (jeśli nie chcesz dodawać - pomiń): ')
    future_alarms.append({
        'future alarm': future_alarm,
        'days_future_alarm': days_future_alarm,
        'how_many_times_future_alarm ': how_many_times_future_alarm,
        'label_of_alarm': label_of_alarm
    })
    return future_alarms

def alarm_turning_off(future_alarms):
    for i, future_alarm in enumerate(future_alarms):
        print(i, future_alarm)
    which_alarm_delete = int(input('Ktory alarm chcesz usunac (podaj indeks): '))
    future_alarms.pop(which_alarm_delete)
    return future_alarms

def do_alarm(future_alarms):
    now = datetime.datetime.now()
    now_str = now.strftime("%H:%M")
    for i in future_alarms:
        if i['future alarm'] == now_str:
            users_snooze = int(input('Ile minut drzemki(jesli nie chcesz to wpisz 0): '))
            snooze_minutes = datetime.timedelta(minutes=users_snooze)
            new_time = now + snooze_minutes
            i['future alarm'] = new_time.strftime("%H:%M")
            if users_snooze < 0:
                duration = 1000 
                frequency = 440  
                winsound.Beep(frequency, duration)

while True:
    do_alarm(future_alarms)
    print('1. Dodaj alarm')
    print('2. Usun alarm')
    print('3. Pokaz alarmy')
    user_answer = int(input('Wybierz opcje: '))
    if user_answer == 1:
        future_alarms = alarm_turning_on(future_alarms)
    elif user_answer == 2:
        future_alarms = alarm_turning_off(future_alarms)
    elif user_answer == 3:
        print(future_alarms)
    else:
        print('Brak takiej opcji')
