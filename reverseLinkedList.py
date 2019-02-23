class LNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
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
    head.next=currt

if __name__=="__main__":
    number =1
    head=LNode(number)
    #head.next=None
    currt=head
    while number<10:
        temp=LNode(number)
        currt.next=temp
        number=number+1
        currt=temp

    print("here is the linked list not reversed")
    currt=head.next
    while currt.next!=None:
        print("{}".format(currt.data))
        currt=currt.next

    reverse(head)
    currt=head.next
    print("here is the linked list after reversed")
    while currt.next!=None:
        print("{}".format(currt.data))
        currt=currt.next


