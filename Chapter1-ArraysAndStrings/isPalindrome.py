#Very small code to check if a string is a palindrom using the collections library
import collections

def isPalindrome(s):
  return sum(v%2 for v in collections.Counter(s).values())<2
  
  
