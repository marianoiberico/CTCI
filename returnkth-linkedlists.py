#Return the kth to last element in a singly linked Linked List

def returnKth(linkedList, k):
  current=runner=linkedList.head
  for i in range(0,k):
    if runner.next==None:
      return None
    runner=runner.next
  
  while runner:
    runner=runner.next
    current=current.next
    
  return current
