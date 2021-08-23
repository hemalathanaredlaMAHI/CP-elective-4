class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        newNode = Node(new_val)
        if (self.root == None):
            self.root = newNode
        else:
            c=self.root
            p=self.root
            while (c!=None):
                p=c
                if (new_val<c.value):
                    c=c.left
                else:
                    c=c.right
            if (new_val<p.value):
               p.left=newNode
            else:
               p.right=newNode
    def printSelf(self):
        print(self.root)
        
    def search(self, find_val):
        while(self.root!=None):
            if(self.root.value==find_val):
                return True
            elif(self.root.value>find_val):
                self.root=self.root.left
            else:
                self.root=self.root.right
        return False

