import datetime, calendar

def getting_name_of_birth_day():
    user_birth_of_day = input('Podaj date urodzenia w formacie np. 1-1-2000: ')
    day, month, year = user_birth_of_day.split('-')
    user_birth_of_day = datetime.datetime(int(year),int(month),int(day))
    return calendar.day_name[user_birth_of_day.weekday()]

def translating_to_polish(getting_name_of_birth_day):
    match getting_name_of_birth_day():
        case 'Monday':
            print('Poniedziałek')
        case 'Tuesday':
            print('Wtorek')
        case 'Wendesday':
            print('Środa')
        case 'Thursday':
            print('Czwartek')
        case 'Friday':
            print('Piątek')
        case 'Saturday':
            print('Sobota')
        case 'Sunday':
            print('Niedziela')
print(translating_to_polish(getting_name_of_birth_day))