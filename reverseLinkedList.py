class LNode:
    """
    The node of linked List
    """
    def __init__(self,data):
        """
        function to generate the LNode Class
        data:the data of the node
        """
        self.data=data
        self.next=None

def reverse(head):
    """
    The function to reverse the linked list, 
    which exchange the next node and the previous node of each element

    head:the start node of the linked list
    """
    if head==None or head.next==None:
        return
    prev,currt,next=None,None,None
    currt=head.next
    next=currt.next
    
    while currt.next!=None:
        next=currt.next
        currt.next=prev
        prev=currt
        currt=next
    currt.next=prev
    head.next=currt

def recursiveReverse(head):
    """
    The same function as reverse but with the recursive methode 
    """
    
    if head is None or head.next is None:
        return head
    else:
        if head.data=="start":
            finalHead=head
            newHead=recursiveReverse(head.next)
            finalHead.next=newHead
            return finalHead
        else:
            newHead=recursiveReverse(head.next)
            head.next.next=head
            head.next=None
            return newHead  

def reverseInsert(head):
    """
    traverse all the elements, the node traversed everytime
    will be inserted after the head node 
    """
    if head is None or head.next is None:
        return 
    currt,next=None,None
    currt=head.next.next
    head.next.next=None    
    while currt!=None:
        tmp=head.next
        head.next=currt
        next=currt.next
        currt.next=tmp
        currt=next
        

if __name__=="__main__":
    
    head=LNode("start")
    #head.next=None
    currt=head
    number =0
    while number<100:
        number=number+1
        temp=LNode(number)
        currt.next=temp        
        currt=temp

    print("here is the linked list not reversed")
    currt=head.next
    while currt!=None:
        print("{}".format(currt.data))
        currt=currt.next

    reverse(head)
    currt=head.next
    print("here is the linked list after reversed")
    while currt!=None:
        print("{}".format(currt.data))
        currt=currt.next
    
    newhead=recursiveReverse(head)
    currt=newhead.next
    print("here is the linked list after recursive reversed")
    while currt!=None:
        print("{}".format(currt.data))
        currt=currt.next

    reverseInsert(newhead)
    currt=newhead.next
    print("here is the linked list after inserting reversed")
    while currt!=None:
        print("{}".format(currt.data))
        currt=currt.next