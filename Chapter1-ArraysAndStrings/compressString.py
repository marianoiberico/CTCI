#Function used to compress string given that there are repetitions in letters

def stringCompression(s):
  output=''
  repeat='1'
  #Add first element 
  output=s[0]
	for i in range(len(s1)-1):
    if s[i]==s[i+1]:
	repeat+=1
    else:
      if(repeat>1):
        output+=str(repeat)
      output+=s[i+1]
      repeat=1
  
  if(repeat>1):
    output+=str(repeat)
		
print(output)
