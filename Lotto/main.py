import random

def getrand():
    min = 1
    max =45
    lottoZahlen1 = []
    lottoZahlen2 = []

    for i in range(min, max):
        lottoZahlen1.append(i)
    
    for i in range(min, max):
        lottoZahlen2.append(i)

    pickednumbArr.clear()
    for i in range(6):
        pickednumb = random.choice(lottoZahlen1)
        lottoZahlen1.remove(pickednumb)
        pickednumbArr.append(pickednumb)
        
    lottoZahlen1.clear()
    lottoZahlen1.append(lottoZahlen2)

def statistik():
    for i in range(1000):
        getrand()

        for e in pickednumbArr:
            stats[e] += 1
    print(stats)


if __name__ == '__main__':
    pickednumbArr= []
    stats= {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
        21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0, 33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0,
        40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0}
    statistik()