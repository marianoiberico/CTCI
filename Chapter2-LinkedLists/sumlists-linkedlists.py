#Sum Two linked lists where the value of the first node represents the 1's value.
from LinkedList import Linked list
def sumLists(l1,l2):
  output = LinkedList()
  carry=0
  n1, n2 = l1.head, l2.head
  while n1 or n2:
    sum=carry
    if n1:
      sum+=n1.value
      n1=n1.next
    if n2:
      sum+=n2.value
      n2=n2.next
    output.add(sum%10)
    carry=sum//10
    
    if carry:
      output.add(carry)
  return output
