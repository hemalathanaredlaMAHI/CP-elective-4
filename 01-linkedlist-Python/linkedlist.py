"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

from typing import Counter


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        p=1
        c=self.head
        if(position<1):
            return None
        while(c and p<=position):
            if(p==position):
                return c
            c=c.next
            p=p+1
        return c


    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        p=1
        c=self.head
        if(position==1):
            new_element.next=self.head
            self.head=new_element
        else:
            while(c and p<position):
                if(p==position-1):
                    new_element.next=c.next
                    c.next=new_element
                c=c.next
                p=p+1



    def delete(self, value):
        """Delete the first node with a given value."""
        c=self.head
        b=None
        while(c.next):
            if(c.value==value):
                if(b):
                    b.next=c.next
                else:
                    self.head=c.next
            b=c
            c=c.next

