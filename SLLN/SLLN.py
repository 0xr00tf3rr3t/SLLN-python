# Single Linked List #

class SingleLinkedListNode(object):

    #Inizializarmos
    def _init_(self, value, nxt):
        self.value = value
        self.next = nxt

    def _repr_(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"
        
        
SLLN=SingleLinkedListNode()
SLLN1=SingleLinkedListNode()

SLLN.value="a"
SLLN1.value="b"
SLLN.nxt=SLLN1
SLLN1.nxt=None
print (SLLN.value)
print(SLLN.nxt.value)

