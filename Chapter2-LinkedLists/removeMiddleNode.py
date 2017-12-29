#This function deletes the middle node which is passed as an argument.

def removeMiddleNode(node):
  node.value=node.next.value
  node.next=node.next.next
