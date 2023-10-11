
#Dziesietny do dwojkowego
def Ten_to_two(number):
    solution = []
    while number>0:
        result = number % 2
        solution.append(result)
        number = number//2
    solution.reverse()
    return solution


#print(Ten_to_two(43))
#wynik trzeba czytac od tylu reverse

#dwojkowy do dziesietnego
def Two_to_ten(number):
    solution = []
    end = 0
    list_number = [int(x) for x in str(number)]
    for x in range(len(list_number)):
       values = list_number.pop()
       result = values * 2**x
       solution.append(result)
    for x in solution:
        end = end + x
    return end
#print(Two_to_ten(101011))
#101011=43



