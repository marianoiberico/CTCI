#Code to check if a pair of strings are one edit away (add,delete or change character) from each other

def oneEditAway(s1,s2):
	if len(s1)<len(s2):
		#Make sure s1 always hold the larger string
    s1,s2 = s2,s1
	if len(s1)-len(s2)>1:
    #If one of them is more than two characters bigger in length then we can immediatly return false
		return false
  elif len(s1)==len(s2):
    #if same length then we have to make sure that strings do not differ by more than one character
		return sum(1 for i in len(s1) if s1(i)!=s2(i))<2
	else:
    #if strings differ in length by exactly one, try discarding one character fromt the longer string and see if they match (all possible permutations)
    for i in len(s1):
			if s1(:i) + s1(i+1:) == s2:
				return true
	return false
