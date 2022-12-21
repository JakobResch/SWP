import random

def median():
    for x in range(len(arr)-1):
        for i in range (len(arr)-x-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
    if len(arr) % 2 == 0:
           index = len(arr)//2
           med = (arr[index -1] + arr[index]) //2 
           print(med)
    else:
        index = len(arr) //2
        med = arr[index]
        print(med)

def durchschnitt():
    summe = 0
    for x in range (len(arr)):
        summe = summe + arr[x]
    durch = summe / len(arr)
    print (durch)

if __name__ == '__main__':
    arr = []
    for x in range (15):
        arr.append(random.randint(1,10))
    print(arr)
median()
durchschnitt()


x = map(median() , arr)
print(x)

class person():
    def __init__ (self, name):
        self.name = name

a1 = person("huber")
print(a1)

