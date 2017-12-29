#function to rotate an nxn matrix when it is passed as an argument (clockwise 90 degrees)

import copy
def rotate(m):
  size=length(m)
  result = copy.deepcopy(m)
  for i in range(size):
    for j in range(size):
      result[j][size-1-i]=m[i]j]
  
  print(result)
