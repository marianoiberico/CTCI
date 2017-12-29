//This function will remove the duplicate nodes in a linked list without using a buffer

def RemoveDup(linkedList):
  if linkedList.head==None:
    return None
  current=linkedList.head
  
  while current:
    runner=current
    while runner.next:
      if runner.next.value==current.value:
				runner.next==runner.next.next
			else:
				runner=runner.next
		current=current.mnext
	
	return linkedList
