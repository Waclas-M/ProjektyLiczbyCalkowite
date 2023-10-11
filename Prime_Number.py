#Did this number is Prime number?
#Prime numer = numer // 1 and // number
def Prime_number(number):
    solution = []
    for x in range(1,number+1):
         remnant = number % x
         if remnant > 0:
             pass
         elif remnant == 0:
             solution.append(remnant)
    if len(solution) == 2:
        return 'liczba pierwsaza'
    else:
        return 'To nie liczba pierwsza'

#print(Prime_number(6))


