# Zeitumrechnung

input_seconds = ''
while True:
    print("Sekunden zum Umrechnen eingeben")
    #366
    input_seconds = input()
    if input_seconds == 'exit':
        break
    foo = int(input_seconds) % 3600
    hours = int(input_seconds) // 3600
    seconds = foo % 60
    minutes = foo // 60
    print("Stunden: {}".format(hours))
    print("Minuten: {}".format(minutes))
    print("Sekunden: {}".format(seconds))

