l=input(" ")
vowel=['a','e','i','o','u','A','E','I','O','U']
if(l>='a' and l<='z') or (l>='A' and l<='Z'):
  if l in vowel:
    print("Vowel")
  else:
     print("Consonant")
else:
  print("invalid")
