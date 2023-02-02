import random

class Node:

    def __init__(self, data):
        ## data of the node
        self.data = data

        ## next pointer
        self.next = None

class LinkedList:

    def __init__(self):
        ## den head als none definieren
        self.head = None

    def insert(self, new_node):
        ## schauen ob head leer ist
        if self.head is None:
            ## wenn head leer ist..
            ## zuweisung des new node zum head
            self.head = new_node

        else:
            ## das erste node wird als last node definiert 
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

            ## Zuweisung des neuen nodes an den nächsten Pointer des letzten nodes
            last_node.next = new_node

    def display(self):
        ## variable für iteration, head (1. Elemten in linked list wird als temp node definiert)
        temp_node = self.head

        ## durchiterieren bis wir am ende sind
        while temp_node != None:
            ## Ausgabe der node
            print(temp_node.data, end='->')

            ## zum mächsten Node springen
            temp_node = temp_node.next

        print('Null')

    def length(self):
        length = 0
        last_node = self.head
        while last_node != None:
                last_node = last_node.next
                length +=1
        print(length)
def home():
    ## Linked list initialisieren
    linked_list = LinkedList()

    ## Daten händisch hinzufügen
    linked_list.insert(Node(1))
    linked_list.insert(Node(2))
    linked_list.insert(Node(3))
    linked_list.insert(Node(4))
    linked_list.insert(Node(5))
    linked_list.insert(Node(6))
    linked_list.insert(Node(7))

	## Nodes linked list über for hinzufügen
    num_of_nodes = int(input("Enter the number of nodes to insert: "))
    min = int(input("What is the min value of the inserted node?: "))
    max = int(input("What is the max value of the inserted node?: "))
    for i in range(num_of_nodes):  
        i = random.randint(min,max)
        linked_list.insert(Node(i))
    
    ## Ausgabe
    linked_list.display()
    linked_list.length()

if __name__ == '__main__':
    home()
