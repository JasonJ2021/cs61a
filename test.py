class LinkedList:
    empty = ()
    def __init__(self,value , next):
        self.value = value 
        self.next = next
    
    def __repr__(self) :
        if(self.next):
            rest_repr = ',' + repr(self.next)
        else:
            rest_repr = ''
        return "LinkedList(" + repr(self.value) + rest_repr + ")"

def filter_link(f, ll):
    """Return a Link that contains only the elements x of Link LL
    for which f(x) is a true value.
    >>> is_odd = lambda x: x % 2 == 1
    >>> filter_link(is_odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if(ll == Link.empty):
        return ()
    if(f(ll.first)):
        return Link(ll.next , filter_link(f,ll.rest))
    else :
        return filter_link(f,ll.rest)
    