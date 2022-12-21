import random

handvalues = []
handsymbols = []
valuecomparisons = []
prozent = []
realProbability = [0.000154, 0.00139, 0.0240, 0.1441, 0.1965, 0.3925, 2.1128, 4.7539, 42.2569, 50.1177]
statistic = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two pairs": 0,
    "Pair": 0,
    "High Card": 0
}


def getsymbol(numbers):
    numbers %= 4
    if numbers == 0:
        return "Heart"
    if numbers == 1:
        return "Club"
    if numbers == 2:
        return "Diamond"
    if numbers == 3:
        return "Spade"


def getcardnumber(number):
    #geht von 0 bis 12 dann 13 bis 25 ergibt auch wieder 0 bis 12 usw. 4Mal da karo,piek,...
    number %= 13
    return number


def getcards(minimum, maximum, amount):
    cards = []
    for g in range(minimum, maximum + 1):
        cards.append(g)
    for j in range(amount):
        randindex = random.randrange(0, maximum)

        lastPosition = len(cards) - 1 - j
        cards[randindex], cards[lastPosition] = cards[lastPosition], cards[randindex]
    return cards[-amount:]



def checkforpairs(values):
    duplicates = [number for number in values if values.count(number) > 1]
    uniques = list(set(duplicates))
    return len(duplicates), uniques


def checkforcombos(symbols, values):
    combo = False
    if symbols.count(symbols[0]) == len(symbols):
        symbols.sort()
        if values[0] == values[-1] - 4 and values[-1] == 12:
            statistic["Royal Flush"] += 1
            combo = True
        elif values[0] == values[-1] - 4:
            statistic["Straight Flush"] += 1
            combo = True
        elif not combo:
            statistic["Flush"] += 1
    if checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) == 1:
        statistic["Four of a Kind"] += 1
        combo = True
    elif checkforpairs(values)[0] == 5 and len(checkforpairs(values)[1]) >= 2:
        statistic["Full House"] += 1
        combo = True
    elif checkforpairs(values)[0] == 3:
        statistic["Three of a Kind"] += 1
        combo = True
    elif checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) >= 2:
        statistic["Two pairs"] += 1
        combo = True
    elif checkforpairs(values)[0] == 2:
        statistic["Pair"] += 1
        combo = True
    values.sort()
    if values[0] == values[-1] - 4 and len(checkforpairs(values)[1]) == 0:
        statistic["Straight"] += 1
        combo = True
    if not combo:
        statistic["High Card"] += 1
def valuecomparison():
    for f in range (10):
        valuecomparisons.append(((prozent[f] - realProbability[f]) / realProbability[f]))
if __name__ == "__main__":
    x = input("How many rounds?")
    x = int(x)
    for x in range(x):
        myCards = getcards(1, 52, 5)
        for i in myCards:
            handvalues.append(getcardnumber(i))
            handsymbols.append(getsymbol(i))
        checkforcombos(handsymbols, handvalues)
        handvalues = []
        handsymbols = []
    
    for i in statistic:
         a = statistic[i] / x * 100
         prozent.append(a)
    valuecomparison()     
    print("Berechnete Wahrscheinlichkeiten:\n",prozent)
    print("Differenz zwischen Berechneten Wslktn und tatsächlichen Wslktn in Prozent:\n",valuecomparisons)


    