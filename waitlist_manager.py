# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None #empty list; head points to first node

    

    def add_end(self,name):
        new_node = Node(name) #creates new node with given value

        if not self.head:   #if list is empty
            self.head = new_node
            return
        else: 
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  #link the last node to the new node

    def add_front(self,name):
        new_node = Node(name)
        if self.head is None: #if list is empty
            self.head = new_node #new node becomes the head
        else:
            new_node.next = self.head #point the new node to the current head
            self.head = new_node #update head to new node



    def remove(self,name):
        current = self.head #start at head
        previous = None     #keep track of previous node
        while current:
            if current.name == name: #check if current node matches the name
                if previous: #if its not the head
                    previous.next = current.next #bypass the current
                else: #if it is the head
                    self.head = current.next #update head to next node
                return
            previous = current
            current = current.next


    def print_list(self):
        current = self.head
        while current: 
            print(current.name, end=" -> ")
            current = current.next
        print("none")





    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program

waitlist_generator()
'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
- What role does the head play?
- When might a real engineer need a custom list like this?
'''
'''
My list works in the following way: 
it first uses a nodes class. this way we can create multiple nodes or in this case customer names. 
Then i created a linked list class to manage the nodes we now can create using the nodes class.
Inside the linked list class contains four different methods which are just functions associated with the specific class they are under.
The methods include an add to front, add to end, print list, and remove from the list.
As the user selects an option whether to add to front, add to end, ect, we call the appropriate method in our linked list class.

The head plays an important part which is always points and is referring to the FIRST node in the list.
If the list is empty, the head is None. It tells you where to start. from there you can follow the next links


A real engineer might need a custom list like this when they need quick insertion/removal at the front.
A linked list might be more efficient than a built in array or list especially because you dont having to slide elements.
Real world scenarios could be at restaurants, hospitals, or airlines. People get added or removed often.





'''