def print_calendar():
    # Set up the dictionary
    months = {1: 'Januar', 2: 'Februar', 3: 'März', 4: 'April', 5: 'Mai', 6: 'Juni', 7: 'Juli', 8: 'August',
              9: 'September', 10: 'Oktober', 11: 'November', 12: 'Dezember'}
    monthdays = {'Januar': 31, 'März': 31, 'April': 30, 'Mai': 31, 'Juni': 30, 'Juli': 31, 'August': 31,
                 'September': 30, 'Oktober': 31, 'November': 30, 'Dezember': 31}
    
    month = int(input("Bitte geben Sie den Monat ein: "))
    
    year = int(input("Bitte geben Sie das Jahr ein: " ))
    
    # Calculate the leap year
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        monthdays['Februar'] = 29
    else:
        monthdays['Februar'] = 28

    # Using Zeller's congruence
    # Change in year if month is January or February
    if 1 <= month <= 2:
        year -= 1
    # Switch months so that March becomes the first month of the year,
    # and January/ February become the 11th and 12th months respectively
    # Convert variables to algorithm variables (so a = month and b = day)
    if month < 3:
        a = month + 10
    else:
        a = month - 2
    b = 7  # The first day of the month
    c = year % 100
    d = year // 100
    # Compute starting weekdays with algorithm
    w = (13 * a - 1) // 5
    x = c // 4
    y = d // 4
    z = w + x + y + b + c - 2 * d
    r = z % 7
    r = (r + 7) % 7

    # Print the title
    space = ' '
    print('\n', space * 6 + months[month] + space + str(year),'\n')
    print("Mo Di Mi Do Fr Sa So")

    # Print out the calendar
    number = monthdays[months[month]]
    start_days = r
    for i in range(1, number + 1):
        if i == 1:
            print((space *3) * start_days, end='')
        if i < 10:
            print('', i, end=' ')
        elif i >= 10:
            print(i, end=' ')
        if (i + start_days) % 7 == 0:
            print('\n', end='')

    if month == 5:
        print('\n \n' '01.05.2022: Tag der Arbeit')
        print('26.05.2022: Christi Himmelfahrt')

print_calendar()
