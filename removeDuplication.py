'''
This program is aimed at removing the replication in a linked list unordered.
The class is the node class to build the list
'''

class LNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def removeDuplication(head):
    '''
    The program takes the head of the linked list as the input parameter
    '''
    if head==None or head.next==None:
        return 

    observedIndex=head.next
    comparedIndex=observedIndex.next
    preComparedIndex=head.next
    while observedIndex!=None:
        comparedIndex=observedIndex.next
        preComparedIndex=observedIndex
        while comparedIndex!=None:
            if observedIndex.data==comparedIndex.data:
                preComparedIndex.next=comparedIndex.next
                comparedIndex=comparedIndex.next
            else:
                preComparedIndex=preComparedIndex.next
                comparedIndex=comparedIndex.next
        observedIndex=observedIndex.next

if __name__ == "__main__":
    head=LNode("Start")
    currt=head
    for i in range(10):
        temp=LNode(i)
        currt.next=temp        
        currt=currt.next

    for i in range(10):
        temp=LNode(i)
        currt.next=temp
        currt=currt.next
    print("The linked list before get rid of duplication")
    currt=head.next
    while currt!=None:
        print(currt.data)
        currt=currt.next
    print("The linked list after get rid of duplication")
    removeDuplication(head)
    currt=head.next
    while currt!=None:
        print(currt.data)
        currt=currt.next 

    
