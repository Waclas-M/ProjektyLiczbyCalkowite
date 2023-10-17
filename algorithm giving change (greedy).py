def greedy_change(cash):
    banknotes = [500,200,100,50,20,10]
    while cash > 0:
        for x in range(len(banknotes)):
            integer = cash // banknotes[x]
            change = cash % banknotes[x]
            cash = change
            print(f"{banknotes[x]} X {integer}")


greedy_change(140)
