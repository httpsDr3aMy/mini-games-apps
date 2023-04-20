measurement = input('Podaj pomiar: (format: 1mm): ')

measurement = measurement.replace(' ', '')
measurement = measurement.lower()

if measurement[-2:] == 'mm':
    millimeter_user = measurement[-2:]
    millimeter_user = measurement.replace('mm', '')
    millimeter_user = int(millimeter_user)
elif measurement[-2:] == 'cm':
    centimeter_user = measurement[-2:]
    centimeter_user = measurement.replace('cm', '')
    centimeter_user = int(centimeter_user)
elif measurement[-2:] == 'dm':
    decymetr_user = measurement[-2:]
    decymetr_user = measurement.replace('dm', '')
    decymetr_user = int(decymetr_user)
elif measurement[-2:] == 'km':
    kilometer_user = measurement[-2:]
    kilometer_user = measurement.replace('km', '')
    kilometer_user = int(kilometer_user)
elif measurement[-1:] == 'm':
    meter_user = measurement[-2:]
    meter_user = measurement.replace('m', '')
    meter_user = int(meter_user)

print('Na co chcesz przekonwertowac?')
print('1. mm')
print('2. cm')
print('3. dm')
print('4. m')
print('5. km')
user_answer = int(input('Wybierz opcje: '))
if user_answer == 1:
    if isinstance(millimeter_user, int):
        millimeter_user = millimeter_user * 0 