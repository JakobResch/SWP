import random
import json

dataFile = {}
weight = [0, 0, 0, 0, 0]
shapes = ["rock", "paper", "scissors", "spock", "lizard"]
countValues = {"player": 0, "cpu": 0, "draws": 0, "rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}

def combine(a, b):
    for key in a:
        dataFile[key] = a[key] + b[key]
    return a

def löschen():
    dataFile = {"player": 0, "cpu": 0, "draws": 0, "rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}
    countValues = dataFile
    weight = [0, 0, 0, 0, 0]
    f = open("data.txt", "w")
    json.dump(dataFile, f)
    f.close()

def speichern():
    f = open("data.txt", "r")
    saved = f.read()
    if saved:
        save_json = json.loads(saved)
        combine(countValues, save_json)
    f.close()
    f = open("data.txt", "w")
    json.dump(dataFile, f)
    f.close()

def ValueCPU():
    count = 0
    for key in dataFile:
        if "player" not in key and "cpu" not in key and "draws" not in key:
            if dataFile[key] == 0:
                weight[count] = dataFile[key] + 0.01
            else:
                weight[count] = dataFile[key]
            count += 1

    move = weight[len(weight) - 1]
    weight.remove(weight[len(weight) - 1])
    weight.insert(0, move)
    choice = random.choices(shapes, k=1, weights=weight)
    return choice[0]


def Winner(player, cpu):
    indexPlayer = shapes.index(player)
    indexCPU = shapes.index(cpu)
    if (indexPlayer + 2) > 4:
        indexPlayer = indexPlayer - 5
    if (shapes[indexPlayer + 2] == shapes[indexCPU]) or (shapes[indexPlayer - 1] == shapes[indexCPU]):
        winner = "DU HAST GEWONNEN!!!"
        countValues["player"] += 1
    elif (shapes[indexPlayer - 2] == shapes[indexCPU]) or (shapes[indexPlayer + 1] == shapes[indexCPU]):
        winner = "CPU gewinnt!"
        countValues["cpu"] += 1
    else:
        winner = "Unentschieden!"
        countValues["draws"] += 1
    return winner


def game():
    speichern()
    beenden = 0
    print("!!Herzliches Willkommen zum erweiterten Stein Schere Papier Spiel!!")
    while beenden == 0:
        print("Wie siehts aus, was willst du machen?")
        print("     Spiel starten --> start")
        print("     Wie ist mein Spiestand? --> statistik")
        print("     Speichere deine Daten --> speichern")
        print("     Lösche deine daten --> neustart")
        print("     Willst du schon aufhören?? --> byeee")
        choice = str(input().lower())
        if choice == "start":
            gameStatus = 1
            print("Das ist das Rock-Paper-Scissors-Spock-Lizard Spiel - LOS GEHTS!!!\n")
            while gameStatus == 1:
                print("Was wählst du? (Rock/Paper/Scissors/Spock/Lizard)")
                shapePlayer = str(input().lower())
                if shapes.count(shapePlayer) == 0:
                    print("Bitte verwende eine Form aus der Liste!")
                else:
                    countValues[shapePlayer] += 1
                    shapeCPU = ValueCPU()
                    countValues[shapeCPU] += 1
                    print("\nDu hast gewählt: ", shapePlayer)
                    print("Die CPU hat gewählt: ", shapeCPU)
                    win = Winner(shapePlayer, shapeCPU)
                    print("\nErgebnis: ", win)
                    counter = 1
                    while counter == 1:
                        print("\nWillst du nochmal spielen? (J/N)")
                        decision = input().lower()
                        if decision == "j":
                            gameStatus = 1
                            counter = 0
                        elif decision == "n":
                            print(countValues)
                            gameStatus = 0
                            counter = 0
                           
                        else:
                            gameStatus = 0
                            counter = 1
                            
            beenden = 0
        elif choice == "löschen":
            löschen()
            speichern()
            print("Deine daten wurden gelöscht\n")
            beenden = 0
        elif choice == "speichern":
            speichern()
            print("Deine daten wurden aktualisiert!\n")
            beenden = 0
        elif choice == "statistik":
            print(dataFile)
            beenden = 0
        elif choice == "byeee":
            print("Schade dass du nicht mehr spielen willst :(")
            beenden = 1
        else:
            beenden = 0
            print("UPS ich glaube du hast dich verschrieben!\n")    

if __name__ == '__main__':
    speichern()
    game()