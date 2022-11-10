import random

handsymbols = []
handvalues = []
#hand = []
lastcard = []
dictPercentage = {'Royal Flush':0,'Straight Flush':0,'Straße':0,'Flush':0,'Full House':0,'Paar':0,'Zwei Paare':0,'Drilling':0,'Vierling':0}
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
        #die gezogene Karte am ende der liste hinzufügen, dMIT MAN sie nicht nochmal ziehen kann#
        lastPosition = len(cards) - 1 - j
        cards[randindex], cards[lastPosition] = cards[lastPosition], cards[randindex]
    return cards[-amount:]


# def convertvalue(value):
    realvalue = value + 2
    if realvalue == 11:
        return "J"
    if realvalue == 12:
        return "Q"
    if realvalue == 13:
        return "K"
    if realvalue == 14:
        return "A"
    return realvalue


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

   
if __name__ == "__main__":
    
    for x in range(10000):
        myCards = getcards(1, 52, 5)
        for i in myCards:
            handvalues.append(getcardnumber(i))
            handsymbols.append(getsymbol(i))
           # hand.append([convertvalue(getcardnumber(i)), getsymbol(i)])
        checkforcombos(handsymbols, handvalues)
        handvalues = []
        handysmbols = []
    prozent = []
    for i in statistic:
         a = statistic[i] / 10000 * 100
         prozent.append(a)
    print(prozent)
    
    

    