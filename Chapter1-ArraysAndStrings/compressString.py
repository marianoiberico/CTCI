#Function used to compress string given that there are repetitions in letters

def dtringCompression(s):

	output=''
  repeat='1'
	//Add first element 
  output=s[0]
	
	for i in range(len(s1)-1):
	  if s[i]==s[i+1] repeat++
		else:
			If(repeat>1) output +=str(repeat)
			Output+=s[i+1]
			Repeat=1
	if(repeat>1):
		output+=str(repeat)
		
print(output)
