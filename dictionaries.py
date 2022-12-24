handy_nummer = input('wie ist deine handynummer : ')

nummeren = {
    '1' : 'eins',
    '2' : 'zwei',
    '3' : 'drei',
    '4' : 'vier',
    '5' : 'fünf',
    '6' : 'sechs',
    '7' : 'sieben',
    '8' : 'acht',
    '9' : 'neun',
    '0' : 'null' 
}
schreiben_von_handy_nummer = ''

for nummer in handy_nummer:
    schreiben_von_handy_nummer += nummeren.get(nummer, 'x') + ' '

print(schreiben_von_handy_nummer)
