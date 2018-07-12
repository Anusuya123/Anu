t=input(" ")
vowel=['a','e','i','o','u','A','E','I','O','U']
if(t>='a' and t<='z') or (t>='A' and t<='Z'):
  if t in vowel:
    print("Vowel")
  else:
     print("Consonant")
else:
  print("invalid")
